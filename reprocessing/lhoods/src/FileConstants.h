#ifndef C_LookupLists
#define C_LookupLists

#include <string>

/*
 *  FILENAMES
 */
/* CONTOURS */
// MC7
const std::string cmsATeps("/home/hep/sr505/mastercode-tools/contour_lookups/mc7/cms_1.1fb_2011.csv");
const std::string atlas0leps("/home/hep/sr505/mastercode-tools/contour_lookups/mc7/atlas_0l_1040pb.csv");
// MC6
const std::string cms_new_at("/home/hep/sr505/mastercode-tools/contour_lookups/mc6/cms_new_at.txt");
const std::string atlas_combined("/home/hep/sr505/mastercode-tools/contour_lookups/mc6/atlas_combined.txt");
// MC5
const std::string cms_nlo_expected("/home/hep/sr505/mastercode-tools/contour_lookups/cms_nlo_expected.txt");
const std::string cms_nlo_observed("/home/hep/sr505/mastercode-tools/contour_lookups/cms_nlo_observed.txt");
const std::string atlas_1l_observed("/home/hep/sr505/mastercode-tools/contour_lookups/atlas-1l_observed.txt");
const std::string atlas_1l_expected("/home/hep/sr505/mastercode-tools/contour_lookups/atlas-1l_expected.txt");
const std::string atlas0l_c1("/home/hep/sr505/mastercode-tools/contour_lookups/atlas-0l_observed.txt");
const std::string atlas0l_c2("/home/hep/sr505/mastercode-tools/contour_lookups/atlas-0l_expected.txt");

/* 1D Lookups */
// MC7
const std::string Bsmumu_LHCb_CMS_CDF_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc7/LHCb_CMS_CDF.dat");
const std::string Bsmumu_LHCb_CMS_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc7/bs_cms_lhcb_s_sb.dat");
const std::string HAtautauEPS_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc7/HA-tautau-eps.csv");
const std::string HAtautau_16_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc7/Htt-CMS-1.6fb.csv");
// MC6
const std::string Bsmumu_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc6/br_bsmumu_enlarged.dat");
const std::string XenonSignal_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc6/xenonSignal_enlarged.dat");
const std::string XenonContour_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc6/xenon_contour.csv");
const std::string HAtautau_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc6/HA-tautau-contour.csv");
const std::string HA_sigbr68_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc6/sig-br-68.csv");
const std::string HA_sigbr95_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc6/sig-br-95.csv");
const std::string HA_sigbr997_file("/home/hep/sr505/mastercode-tools/1d_lookups/mc6/sig-br-99-7.csv");


/*
 *  STANDARD CHI2 VALUES
 */
const double chisq_68percent_1d(0.9889464815);
const double chisq_68percent_2d(2.2788685664);
const double chisq_95percent_1d(3.8414588207);
const double chisq_95percent_2d(5.9914645471);
const double chisq_99percent_1d(6.6348966010);
const double chisq_99percent_2d(9.2103403720);

/*
 *  SPECIFIC CHI2 VALUES
 */
const double cms_alphat_chisq_exp(4.26);
const double cms_chiinf(0.85);
const double atlas_1l_chisq_exp(9.1);
const double atlas_1l_chiinf(1.2);
const double atlas_0l_chiinf(0.35);

#endif /* C_LookupLists */
