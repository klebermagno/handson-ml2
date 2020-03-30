#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Python standard-library
from urllib.parse import urlencode
from urllib.request import urlretrieve

# Third-party dependencies
from astropy import units as u
from astropy.coordinates import SkyCoord
from IPython.display import Image


# In[8]:



# initialize a SkyCood object named hcg7_center at the location of HCG 7
hcg7_center = SkyCoord.from_name('HCG 7')
#red.header['LATOBS'] = "32:11:56" # add spurious header info
#red.header['LONGOBS'] = "110:56"
print(SkyCoord('14h04m07.218s', '54d18m03.72s', frame='icrs'))
print(hcg7_center.ra, hcg7_center.dec)
print(hcg7_center.ra.hour, hcg7_center.dec)


# In[ ]:


# tell the SDSS service how big of a cutout we want
#http://learn.astropy.org/rst-tutorials/coordinates.html?highlight=filtertutorials
#hubble https://hla.stsci.edu/cgi-bin/display?image=hlsp_appp_hst_wfpc2_sfd-pu4k2ho01_f606w_v2_sci&izoom=1.000000&detector=WFPC2&aperture=%20&title=appp_hst_wfpc2_sfd-pu4k2ho01%20WFPC2%20F606W%20(hlsp)%20APPP
#https://hla.stsci.edu/hlaview.html#Inventory|filterText%3D%24filterTypes%3D|query_string=14%2003%2012.6%20%2B54%2020%2056.7%20r%3D0.2d&posfilename=&poslocalname=&posfilecount=&listdelimiter=whitespace&listformat=degrees&RA=210.802500&Dec=54.349083&Radius=0.200000&inst-control=all&inst=ACS&inst=ACSGrism&inst=WFC3&inst=WFPC2&inst=NICMOS&inst=NICGRISM&inst=COS&inst=WFPC2-PC&inst=STIS&inst=FOS&inst=GHRS&imagetype=best&prop_id=&spectral_elt=&proprietary=both&preview=1&output_size=256&cutout_size=12.8|ra=&dec=&sr=&level=&image=&inst=ACS%2CACSGrism%2CWFC3%2CWFPC2%2CNICMOS%2CNICGRISM%2CCOS%2CWFPC2-PC%2CSTIS%2CFOS%2CGHRS&ds=

im_size = 12*u.arcmin # get a 12 arcmin square
im_pixels = 1024 
cutoutbaseurl = 'http://skyservice.pha.jhu.edu/DR12/ImgCutout/getjpeg.aspx'
query_string = urlencode(dict(ra=hcg7_center.ra.deg, 
                              dec=hcg7_center.dec.deg, 
                              width=im_pixels, height=im_pixels, 
                              scale=im_size.to(u.arcsec).value/im_pixels))
url = cutoutbaseurl + '?' + query_string

print(url)
# this downloads the image to your disk
urlretrieve(url, 'HCG7_SDSS_cutout-2.jpg')
#http://archives.esac.esa.int/hsa/whsa/
#https://sha.ipac.caltech.edu/applications/Spitzer/SHA//#id=SearchByPosition&RequestClass=ServerRequest&DoSearch=true&SearchByPosition.field.radius=0.13888889000000001&UserTargetWorldPt=9.83;0.8880555555555555;EQ_J2000&SimpleTargetPanel.field.resolvedBy=nedthensimbad&MoreOptions.field.prodtype=aor,pbcd,bcd,irsenhanced,supermosaic,sourcelist,inventory&InventorySearch.radius=0.13888889000000001&shortDesc=Position&isBookmarkAble=true&isDrillDownRoot=true&isSearchResult=true
#http://learn.astropy.org


# In[31]:


Image('HCG7_SDSS_cutout.jpg')


# In[ ]:




