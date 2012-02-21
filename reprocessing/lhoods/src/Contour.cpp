#include "Contour.h"
#include <iterator>

bool Contour::populate_contour(std::string filename)
{
    if(segment_data.size()>0) 
    {
        std::cout << "non-empty contour being populated, clearing data" << std::endl;
        segment_data.clear();
    }
    std::stringstream file_name_stream;
    if(filename!="") {
        file_name_stream << filename;
    }
    else 
    {
        std::cout << "no file name provided for contour" << std::endl;
        return false;
    }
    std::ifstream file_in(file_name_stream.str().c_str());
    if (!file_in) 
    {
        std::cout << "Error while trying to open file `" << file_name_stream.str()
            << "`, file not found" << std::endl;
        return false;
    }
//    std::cout << "Opened " << file_name_stream.str() << std::endl;
    double x,y;
    PolCoord p_temp1, p_temp2;

    //read first line
    if(file_in >> x >> y)
    {
        double r = sqrt(x*x+y*y);
        double theta = atan(y/x);
        p_temp1 = PolCoord(r,theta);
        min_r = p_temp1.r;
        max_r = p_temp1.r;
    }
    //read rest of file 
    while( file_in >> x >> y )
    {
        p_temp2 = p_temp1;
        p_temp1.r = sqrt(x*x+y*y);
        p_temp1.theta = atan(y/x);

        Segment s(p_temp1,p_temp2); 
        // most efficient if we pick up on maximum r here, otherwise we have to
        // double check every point later as we are only sorting by theta
        if(p_temp1.r < min_r ) min_r = p_temp1.r;
        if(p_temp1.r > max_r ) max_r = p_temp1.r;
        segment_data.push_back(s);
    }
    file_in.close();

    // sort by data by ascending theta
    std::sort(segment_data.begin(),segment_data.end(),SegmentAscendingSort());

    // assign max and min values for comparison later
    // this is guaranteed as each segment has it's points ordered theta1<theta2
    // p1->p2; and then the segments are sorted by their theta1
    min_theta = segment_data.front().begin.theta;
    max_theta = segment_data.back().end.theta;

    return true;
}

bool Contour::in_contour(double r, double theta)
{
    if(segment_data.empty())
    {
        std::cout << "Attempted to work with an empty contour" << std::endl;
        return false;
    }

    // initial checks: does it lie in the range that the contour covers at
    // extrema - 
    if( theta > max_theta || theta < min_theta ) return false;
    // for future reference the above may not work if we have a closed contour
    // around the origin in all +/- planes.

    // now need to find all possible segments with theta_min < theta_point
    PolCoord point(r,theta);
    std::vector<Segment>::iterator u_bound;
    u_bound = lower_bound( segment_data.begin(), segment_data.end(), point , SegmentLessThan());

    int intersects=0;
    for( std::vector<Segment>::iterator it = segment_data.begin(); it!=u_bound; ++it )
    {
        // max theta of segment (second point) > theta => theta lies in segment
        if(it->end.theta > theta )
        {
            /* does it actually cross the segment */
            // construct a triangle defining the segment      
            double r1 = it->begin.r;
            double r2 = it->end.r;
            double theta1 = it->begin.theta;
            double theta2 = it->end.theta;
            // segment length l
            double l = sqrt(r1*r1 + r2*r2 - 2*r1*r2*cos(theta2-theta1));
            // alpha: angle between segment and r1 (segment pt with lowest theta)
            double sin_alpha = r2*sin(theta2-theta1)/l;
            // new triangle constructed using a line to the point begin checked
            // bisecting the segment triangle.  gamma is the angle between the segment
            // and the bisection.
            double gamma = M_PI-(theta - theta1) - asin(sin_alpha);
            // R: length of the bisection: i.e. length of line to reach segment at
            // angle theta
            double R = r1*sin_alpha/sin(gamma);
            // our point is further away than this line.
            if(r>R) intersects++;
        }
    }

    // if the contour doesnt' cover the origin:
    //  even intercepts => outside contour or in a hole
    //  odd intercepts  => inside contour
    //    Our count is fine.
    // if the contour covers the origin
    //  even intercepts => inside contour
    //  odd intercepts  => outisde contour
    //    Need to increment our count
    //std::cout<< "detected " << intersects << " segment intersects" << std::endl;


    // logically ++/-- doesn't matter, but care about % operator doing (-ve)%2
    // being safe
    if(include_origin) 
    {
        intersects++;
    }
    // even/odd check
    int is_in_contour = intersects%2;

    return(is_in_contour);
}

//calculates the closest approach of a point to another point on the contour
double Contour::min_distance(double r, double theta)
{
    if(segment_data.empty())
    {
        std::cout << "Attempted to work with an empty contour" << std::endl;
        return -1.;
    }

    double closest = std::numeric_limits<double>::max();
    double r1_point, r2_point, theta1_point ,theta2_point, l, l1,l2;
    std::vector<Segment>::iterator it_closest;

    // calculate the nearest segment by minimum average distance from segments
    // defining points
    for( std::vector<Segment>::iterator it = segment_data.begin();
            it != segment_data.end(); ++it )
    {
        r1_point = it->begin.r;
        r2_point = it->end.r;
        theta1_point = it->begin.theta;
        theta2_point = it->end.theta;
        l1 = sqrt( r*r + r1_point*r1_point - 2*r*r1_point*cos(theta-theta1_point));
        l2 = sqrt( r*r + r2_point*r2_point - 2*r*r2_point*cos(theta-theta2_point));
        l = (l1 + l2) / 2.;
        if( l < closest )
        {
            closest = l;
            it_closest = it;
        }
    }
    // now have closest segment. 
    // what is the closest approach to this segment
    closest = point_to_segment(r,theta,*it_closest);
    return closest;
}

// returns the distance to the linearly interpolated contour at a given theta
double Contour::get_R(double theta)
{
    // first thing to do: find segment that theta lies in
    std::vector<Segment>::iterator seg;
    for( std::vector<Segment>::iterator it = segment_data.begin();
            it != segment_data.end() && it->begin.theta<theta; it ++ )
    {
        seg = it;
    }
    /*
       std::cout << "found in range: " << (*seg).first.first << " to " 
       << (*seg).second.first << std::endl;
       */  
    double r1 = seg->begin.r, r2 = seg->end.r;
    double t1 = seg->begin.theta, t2 = seg->end.theta;

    double x1 = r1*cos(t1), y1 = r1*sin(t1);
    double x2 = r2*cos(t2), y2 = r2*sin(t2);

    double m_seg = (y1-y2)/(x1-x2);
    double x_intercept = (m_seg*x1 - y1)/(m_seg - tan(theta));
    // important - m_seg -> +-inf if x1==x2, so fix x_intercept
    if(x1==x2) x_intercept = x1;
    double y_intercept = x_intercept * tan(theta);


    /*  std::cout << "Intercept with segment: (x,y) = " 
        << x_intercept << "," << y_intercept << std::endl
        << "(r,theta) = "
        << sqrt(x_intercept*x_intercept+y_intercept*y_intercept)
        << "," << atan(y_intercept/x_intercept) << std::endl;
        */ 
    double R = sqrt(x_intercept*x_intercept+y_intercept*y_intercept);
    return R;
}


double Contour::point_to_segment(double r, double theta, Segment& s)
{
    return point_to_segment(r,theta,s.begin.r,s.begin.theta,
            s.end.r,s.end.theta);
}

// For a point P and line segment AB, returns the distance P is from AB
double Contour::point_to_segment(double Pr, double Pt, double Ar, double At,
        double Br, double Bt)
{
    // convert to cartestians - easier for straight line calculations
    double Px = Pr*cos(Pt);
    double Py = Pr*sin(Pt);
    double Ax = Ar*cos(At);
    double Ay = Ar*sin(At);
    double Bx = Br*cos(Bt);
    double By = Br*sin(Bt);

    // r describes the position of point R (the intersection of the perpendicular
    // line from AB->P) along AB.  It should be AP dot AB / |AB|^2
    double r_num = (Px-Ax)*(Bx-Ax) + (Py-Ay)*(By-Ay);
    double r_den = (Bx-Ax)*(Bx-Ax) + (By-Ay)*(By-Ay);
    double r= r_num / r_den;

    // see above for description of R
    //double Rx = Ax + r*(Bx-Ax);
    //double Ry = Ay + r*(By-Ay);

    // indicates the location along RP, i.e. relation of P to AB
    double s = ( (Ay-Py)*(Bx-Ax) - (Ax-Px)*(By-Ay) ) / r_den;

    double distance_to_line = fabs(s)*sqrt(r_den);

    double distance_to_segment = 0;
    if ( (r >= 0) && (r <= 1) )
    {
        distance_to_segment = distance_to_line;
    }
    else
    {
        double d1 = (Px-Ax)*(Px-Ax) + (Py-Ay)*(Py-Ay);
        double d2 = (Px-Bx)*(Px-Bx) + (Py-By)*(Py-By);

        distance_to_segment=(d1<d2)?sqrt(d1):sqrt(d2);
    }

    return distance_to_segment;
}

double Contour::get_Theta(double x)
{
    std::vector<Segment>::iterator seg;
    for( std::vector<Segment>::iterator it = segment_data.begin(); it != segment_data.end() ; ++it ) 
    {
        double xval1 = it->end.r*cos(it->end.theta);
        double xval2 = it->begin.r*cos(it->begin.theta);

        if( x>=xval1 && x<=xval2 ) seg = it;
    }
    //  double xmin = seg->second.second*cos(seg->second.first);
    //  double xmax = seg->first.second*cos(seg->first.first);

    // seg should now point to the segment in which the point lies
    double theta = M_PI/2.; // set to default to protect against x=0 problem
    if(x>0) 
    {
        double r1(seg->begin.r),r2(seg->end.r);
        double t1(seg->begin.theta), t2(seg->end.theta);
        double x1( r1*cos(t1) ), y1( r1*sin(t1) );
        double x2( r2*cos(t2) ), y2( r2*sin(t2) );

        double y = ((y2-y1)/(x2-x1))*(x-x1) + y1;
        theta = atan(y/x);
    }
    return theta;
}

int Contour::getSegmentIndex(double theta)
{
    std::vector<Segment>::iterator seg = segment_data.begin();
    for( std::vector<Segment>::iterator it = segment_data.begin(); it!=segment_data.end(); ++it )
    {
        if(it->begin.theta<theta && it->end.theta>theta) seg = it;
    }
    return std::distance(segment_data.begin(),seg);
}

bool Contour::print()
{
    if(segment_data.empty())
    {
        std::cout << "Attempted to print an empty contour" << std::endl;
        return false;
    }
    double r,t;
    std::cout <<  "=========================" << std::endl;
    std::cout <<  "|   theta   |     r     |" << std::endl;
    std::cout <<  "=========================" << std::endl;
    for( std::vector<Segment>::iterator it = segment_data.begin();
            it != segment_data.end(); ++it )
    {
        t = it->begin.theta; r = it->begin.r;
        std::cout<< "|" << std::setw(11) << t << "|" << std::setw(11) << r << "|" << std::endl;
        t = it->end.theta;r = it->end.r;
        std::cout<< "|" << std::setw(11) << t << "|" << std::setw(11) << r << "|" << std::endl;
        std::cout<< "-------------------------" << std::endl;
    }
    std::cout<< "Max(min) theta: " << max_theta << "(" << min_theta <<")" << std::endl;
    std::cout<< "Max(min) r    : " << max_r << "(" << min_r << ")" << std::endl;
    return true;
}
