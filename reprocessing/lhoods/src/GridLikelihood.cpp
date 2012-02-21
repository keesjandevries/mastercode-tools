#include "GridLikelihood.h"

// probably just needs to be getNumberEvents
double GridLikelihood::getNumberEvents(double x, double y)
{
  if(plane_.isInPlane(x,y)) {
    //std::cout<<"inGrid:";
    //return getEventsInterpolateGrid(x,y); 
    return getEventsWeightedGrid(x,y);
  } else {
    //std::cout<<"reScale:";
    return getEventsRescaled(x,y);
  }
}

double GridLikelihood::getEventsInterpolateGrid(double x, double y)
{
  ThreePointPlane delaunay;
  setPlane(delaunay,x,y);
  ThreeVector point(x,y,0);
  return delaunay.getMissingComponent(point);
}

double GridLikelihood::getEventsWeightedGrid(double x, double y)
{
  ThreePointPlane weighter;
  setPlane(weighter,x,y); 
  ThreeVector point(x,y,0);
  return weighter.getWeightedContribution(point);
}

void GridLikelihood::setPlane(ThreePointPlane& tpp, double x, double y)
{
  _v_ER_it region = plane_.getRegion(x,y);
  if( plane_.isEnd(region) ) {
    std::cout << "Failure in finding appropriate region in"
    "GridLikelihood::getEventsWeightedGrid" << std::endl;
    return ;
  }
  std::pair<_v_ER_it, _v_ER_it> neighbours = plane_.getNeighbours(x,y,region);
  if(plane_.isEnd(neighbours.first) || plane_.isEnd(neighbours.second))
    { std::cout<< "*** failed to find neighbours" << std::endl; }

  ThreeVector J = region->getThreeVector();
  ThreeVector K = neighbours.second->getThreeVector();
  ThreeVector I = neighbours.first->getThreeVector();

  tpp = ThreePointPlane(I,J,K);
}

double GridLikelihood::getEventsRescaled(double x, double y)
{
  // x,y: actual point
  // xR, yR: point on edge of grid radial line bisects

  VertexIntercept vInt = getLastIntercept(x,y);
  if(plane_.isEnd(vInt.region_)) return -1.;

  double xR=vInt.xint_;
  double yR=vInt.yint_;
  //std::cout<<"{"<<xR<<","<<yR<<"}";

  std::pair<_v_ER_it,_v_ER_it> neighbours=plane_.getNeighbours(x,y,vInt.region_);

  ThreeVector J = vInt.region_->getThreeVector();
  ThreeVector K = neighbours.second->getThreeVector();
  ThreeVector I = neighbours.first->getThreeVector();

  ThreePointPlane delaunay(I,J,K);
  
  double edge_events = -1.;
  if(areCollinear(I,J,K)) {
   // std::cout<<"--C--";
    std::pair<double,double> intercepts = delaunay.getLinearIntercept(x,y);
    xR = intercepts.first; yR = intercepts.second; // xR,yR are now the points
//    std::cout<<"c: " << x << "," << y << std::endl;
    // where the radial line through x,y intercept our linear `plane`
  } 
  // getMissing components is resiliant to collinearity
  ThreeVector point(xR,yR,0);
  edge_events = delaunay.getMissingComponent(point);
  return doRescale(x,y,xR,yR,edge_events); 
}

// returns the last region and x,y intercept point of a radial line thorugh the grid
VertexIntercept GridLikelihood::getLastIntercept(double x,double y)
{
  std::vector<_v_ER_it> intersects = plane_.getIntersects(x,y);

  if(intersects.size()==0) {
    return VertexIntercept(plane_.getEnd(),0,0);
  }

  VertexIntercept vInt(plane_.getEnd(),0,0);
  double rsq(-1.);
  for( std::vector<_v_ER_it>::iterator it = intersects.begin();
       it != intersects.end(); ++it ) {
    bool top(false),side(false);
    double rint_sq = -1.;
    double yint = (*it)->getXmax()*(y/x);
    double xint = (*it)->getYmax()*(x/y);
    if(yint < (*it)->getYmax() && yint > (*it)->getYmin() ) {
      rint_sq = yint*yint + (*it)->getXmax()*(*it)->getXmax();
      side=true;
    } else if(xint < (*it)->getXmax() && xint > (*it)->getXmin()) {
      rint_sq = xint*xint + (*it)->getYmax()*(*it)->getYmax();
      top=true;
    }
    if(rint_sq > rsq) {
      rsq = rint_sq;
      vInt.region_ = *it;
      if(top) { vInt.yint_=vInt.region_->getYmax(); vInt.xint_=xint; }
      if(side){ vInt.xint_=vInt.region_->getXmax(); vInt.yint_=yint; }
    }
  }
  return vInt;
}

double GridLikelihood::doRescale(double x, double y, double xR,
                                  double yR, double edge_events)
{
  double R_rescaleSq = xR*xR + yR*yR;
  double R_pointSq = x*x + y*y;
  double rescale_events = edge_events *
    (R_rescaleSq/R_pointSq)*(R_rescaleSq/R_pointSq);
  return rescale_events;
}

double GridLikelihood::getChi2(double x, double y)
{
    double glpv = (*it)->getPval(x,y); 
    double glchi2 = 0;
    if(glpv<1.) { 
      glchi2 = TMath::ChisquareQuantile(glpv,2.);
    } else if (glpv==1) {
      glchi2 = 1e9;
    }
}

double GridLikelihood::get1DChi2(double x,double y)
{
  double events = getNumberEvents(x,y);
//  std::cout << events << ":"; 
  if(events<0) return 0.;
  double chi2 = (events-mu_)/sigma_;
  chi2*=chi2; //square it
  return chi2;
}

double GridLikelihood::getNSigma(double x, double y)
{
  double events = getNumberEvents(x,y);
  //std::cout<< "*" << events << "*";
  if(events<0) return 0;
  return (events-mu_)/sigma_; 
}

double GridLikelihood::getNormalCDF(double x, double y)
{
  double events = getNumberEvents(x,y);
  double Earg = (events-mu_)/(sqrt(2*sigma_*sigma_));
  double cdf = 0.5*(1+erf(Earg));
  return cdf;
}

double GridLikelihood::getPval(double x, double y)
{
  double nCDF = getNormalCDF(x,y);
  double pval = nCDF*2.-1.;
  return pval;
}
