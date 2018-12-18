import pytesseract
from PIL import Image
import os
import cv2
from io import StringIO
#需要安装Tesseract-OCR
#要装环境变量
#pytesseract中的tesseract_cmd变成tesseract安装的地址E:/gogogopython/venv/Tesseract-OCR/tesseract.exe
# C盘访问不到的话容易出现权限错误
#https://blog.csdn.net/dcrmg/article/details/78233459?locationNum=7&fps=1  训练的方法

path='E:/pic/222/'
deletepath='E:/pic/111/picture/2018/12/05/'
outpathl='E:/pic/222/l/'
#Dou
print(pytesseract.image_to_string(Image.open(path+'8888.jpg'), lang='eng'))

listcontain=[]
listcontain2=[]

# for files in os.listdir(path):
#     image = cv2.imread(path+files)
#     cropImg = image[10:200,10:200]
#     cv2.imwrite(outpathl+'9999.jpg',cropImg)
print(pytesseract.image_to_string(Image.open(outpathl+'9999.jpg'), lang='eng'))



# for files in os.listdir(outpathl):

#     f=pytesseract.image_to_string(Image.open(outpathl+files), lang='chi_dy3')
#     if(str(f).find("饕")>=0)and(str(f).find("音")>=0):
#         # os.remove(deletepath+files)
#         listcontain.append(files)
#     # elif(str(f).find("音")>=0)and(str(f).find("饕")>=0):
#     #     listcontain.append(files)
#     elif(str(f).find("抖")>=0)and(str(f).find("饕")>=0):
#         listcontain.append(files)

# for files in os.listdir(deletepath):
#     if files not in listcontain:
#         os.remove(deletepath+files)


w=StringIO()

setlist=['0344e15a2f634d93b1757ef268717527.mp4.jpg', '058e9017708c43618a990d95ac36374b.mp4.jpg', '05bf15de5c2149ef9b5c3f2e5e1f7cba.mp4.jpg', '07930e0a0b4e4619a986636cbd523d8e.mp4.jpg', '0a637f7cdbb948258c2b1b7619c39e2e.mp4.jpg', '14828a6fbb644d84a69c4a78235ce164.mp4.jpg', '15516baef44e48e485b54310e1934f29.mp4.jpg', '175546e76a844a56a914b2cc6d427466.mp4.jpg', '1b0ee235cfae4812bc126820e3bca1ad.mp4.jpg', '1f77fbf0176845d797ce354d196a6d74.mp4.jpg', '2c2a6614b91b472fb836b1bb6175fabd.mp4.jpg', '2f06d328d4164b148ba9dfa33ef45c01.mp4.jpg', '3db3cd3792114c6ca02c28f2d3873d26.mp4.jpg', '3e95b0e0c6aa499db093df8b4d7db84d.mp4.jpg', '3f99ae6081134098b090aff70d7af61a.mp4.jpg', '470b68c4093745f297d94c62374e380c.mp4.jpg', '4aec96de94f448d4b1953f75279ff06d.mp4.jpg', '4c0e7a92ae38466ea817baaa77121268.mp4.jpg', '510dc78c65cc40caa3cdcc8b56b589df.mp4.jpg', '55cec5d873ec4ba8af5f1708f67896ec.mp4.jpg', '56f02f08cb7546c2a8ba1b40e2c057ff.mp4.jpg', '65a502c9e5bd4ce1a1d486ebaee721ee.mp4.jpg', '6631ba33ea7c43878e1b17845c4061a2.mp4.jpg', '6713d244459045ea9aff7375f757383f.mp4.jpg', '6e8880c408c14360a4f6392246e95486.mp4.jpg', '6ff471db2aad47c3b6dfc6189078e173.mp4.jpg', '7d1cfe5ecb3e4158991b12a89099704d.mp4.jpg', '8025dcf38b8b43a9b9fe3ce598aa8a8f.mp4.jpg', '8231c95ca9d34d83a4bba1e3071af971.mp4.jpg', '85f1ef3f822e4fd38a26826d7db00cd4.mp4.jpg', '99f36806becb426885a14a14ab2656d0.mp4.jpg', 'aa3d252bd5c944f68cd958cb8c468559.mp4.jpg', 'ad1884d1bb8b4a99a50488714705f60a.mp4.jpg', 'b46ff4a8974b43059cc31d930694cc5c.mp4.jpg', 'b807d8d9dcd84b079a3e046243489d0a.mp4.jpg', 'bfb4fe002c674097bd5d1a7c46f6b128.mp4.jpg', 'c3fe46d3be3046ab9c14cb31e0c4484b.mp4.jpg', 'ce306b19cd234cea98d607ebf1c7879a.mp4.jpg', 'd1525d224b564d4ebe42cabd8b42279f.mp4.jpg', 'd1f10e79d9df43f48807491cf147065a.mp4.jpg', 'df5a6fd22470466b953b3d55bda0e13a.mp4.jpg', 'e6047837e9824c5597741e5a890ad3be.mp4.jpg', 'e6d0709ec3d14fe2bf9fc840d55e74d9.mp4.jpg', 'ece52f996d8d4d79aaab8e00a6034e06.mp4.jpg', 'f16cab2473bf4fff8052da0c687ff8a7.mp4.jpg', 'f1fb26f4acdc448997920b61497a563f.mp4.jpg', 'fa2aa83a0bef4895be59dbd292e097b2.mp4.jpg', 'fbd1bf0c083246e1bdee58d172fcd3b4.mp4.jpg', 'fd540fe6239c44178a3c438d0a459e7e.mp4.jpg', 'fdc68f17ecc6440ea0e6a9799032de15.mp4.jpg', 'v0200f000000bbir7oo9lr7020mvtjg0.mp4.jpg', 'v0200f000000bbna27aikatmr9ca0g00.mp4.jpg', 'v0200f000000bdumq7k0gfkji5fq5ug0.mp4.jpg', 'v0200f000000bdv0f5c0gfkji5fqgi30.mp4.jpg', 'v0200f040000bemclblahtmfgmv4s1hg.mp4.jpg', 'v0200f040000bemrf8ubn5v941l3tnv0.mp4.jpg', 'v0200f060000bblukmevld72mogs56eg.mp4.jpg', 'v0200f060000bbna1euvld72mogtpa2g.mp4.jpg', 'v0200f0b0000behi5kv3cp50750ketj0.mp4.jpg', 'v0200f0b0000beisrba0ifkv0dvn49f0.mp4.jpg', 'v0200f0b0000bej1slk1n3e0vundo640.mp4.jpg', 'v0200f0b0000bejed72mac2pmier9gf0.mp4.jpg', 'v0200f0b0000bemh70pq4do14c3kksi0.mp4.jpg', 'v0200f0e0000bcrjirudm151e9o3v4kg.mp4.jpg', 'v0200f0f0000bdqm8v1cgf31f36ncgg0.mp4.jpg', 'v0200f150000be4c6kedm15fa9ddhafg.mp4.jpg', 'v0200f180000bbo7rpiepr17h5mikjog.mp4.jpg', 'v0200f180000bc3cact8n75uip1n644g.mp4.jpg', 'v0200f180000bd2vp0aikatmh1c1p0ig.mp4.jpg', 'v0200f180000bda7v5sps0slndi2rg90.mp4.jpg', 'v0200f180000bdlepgaepr17h5jjik40.mp4.jpg', 'v0200f180000bdo04qo9lr7ddjbfk7m0.mp4.jpg', 'v0200f180000bdocluaikatmh1dgrdjg.mp4.jpg', 'v0200f180000bdp54qsps0slndjdbs8g.mp4.jpg', 'v0200f190000bc3dnqagnbh5ublodiug.mp4.jpg', 'v0200f190000bclnu959688r6fohe9tg.mp4.jpg', 'v0200f190000bcocs0t9688r6fonvung.mp4.jpg', 'v0200f190000bd80apl9688r6fpt9u00.mp4.jpg', 'v0200f190000bd80tdfff77bgc1s8290.mp4.jpg', 'v0200f190000bdaptm32ap9c7pu5qk80.mp4.jpg', 'v0200f190000bddv7brrh3p0ipalnmbg.mp4.jpg', 'v0200f1d0000beh2ctkmavfb00pl450g.mp4.jpg', 'v0200f1d0000bejoogclbum1rmm3sff0.mp4.jpg', 'v0200f1d0000bekras2gd9fjkmfa163g.mp4.jpg', 'v0200f1e0000beosfn4lbumclsnt73gg.mp4.jpg', 'v0200f220000be7ne22iv576h6m1ocsg.mp4.jpg', 'v0200f220000bfd7ju9evctpmf8lod5g.mp4.jpg', 'v0200f240000bfla55rc86dva7t2dofg.mp4.jpg', 'v0200f2e0000bbmintpcgf3b0un8iagg.mp4.jpg', 'v0200f2e0000bbmiohcthbi7htaosu20.mp4.jpg', 'v0200f310000bbigu17k43ap8prushmg.mp4.jpg', 'v0200f310000bbkn9rc0gfknp8iqa4a0.mp4.jpg', 'v0200f310000bblf7vc81ukue8jos0u0.mp4.jpg', 'v0200f320000bdr9shjcp23e7a0mooeg.mp4.jpg', 'v0200f320000bdv8l47ff77bq76n0u1g.mp4.jpg', 'v0200f3e0000bei7u9gghl0kh792guo0.mp4.jpg', 'v0200f3e0000bekadtqepr16l8lq0ftg.mp4.jpg', 'v0200f3e0000ben48lbbo1ieflffd7ng.mp4.jpg', 'v0200f410000bg2fv4l1mik5fkc5boeg.mp4.jpg', 'v0200f490000bfv0rcet8ah1j3klsbg0.mp4.jpg', 'v0200f500000bdj68eulg9ji6ldndte0.mp4.jpg', 'v0200f500000befnor8ckqbr88cf1eo0.mp4.jpg', 'v0200f530000bdhv025f1stetq0pdic0.mp4.jpg', 'v0200f570000bf06k1l8n75l9iqe0k10.mp4.jpg', 'v0200f5b0000bds3rp4ps0srkr4fjsug.mp4.jpg', 'v0200f5c0000bdr1ptigd9fhlsk1b6n0.mp4.jpg', 'v0200f5c0000bdroq3nrri6coboemkgg.mp4.jpg', 'v0200f5e0000bf0ca3qiv579d5vnvig0.mp4.jpg', 'v0200f620000bfsjq7dd2r6c4roaig8g.mp4.jpg', 'v0200f660000bbupkrkpg623e2rop5bg.mp4.jpg', 'v0200f660000bcnq55cpg623e2u36qdg.mp4.jpg', 'v0200f660000bdbg0toa2pejvu2b7oeg.mp4.jpg', 'v0200f660000bdgej911h1vp41j3bkbg.mp4.jpg', 'v0200f680000bejmp849hq5vavk193ag.mp4.jpg', 'v0200f6b0000bfqkef0697anvc8t2tig.mp4.jpg', 'v0200f700000bft652rd82dof8u6q6ug.mp4.jpg', 'v0200f740000bem4ul2kr6g9m0d35tt0.mp4.jpg', 'v0200f780000bc4mqg7iv42bmomho6g0.mp4.jpg', 'v0200f790000bef2ea5f1st31gq3sfh0.mp4.jpg', 'v0200f790000bei4i4hum7ltltp58cfg.mp4.jpg', 'v0200f790000bejhn9fl54d6jphr17pg.mp4.jpg', 'v0200f7d0000bbir6jc9hq5h123gk4n0.mp4.jpg', 'v0200f860000bf25ar72gdds0jvqtgog.mp4.jpg', 'v0200f890000bdratdt81shmbn1gde00.mp4.jpg', 'v0200f890000bdufqphpjc2pb6g7e2r0.mp4.jpg', 'v0200f890000bf9844nrri60j27e38b0.mp4.jpg', 'v0200f8d0000bfbdu4feqk8e7iu0e7vg.mp4.jpg', 'v0200f8e0000bdv3apbc86dssbc4jb1g.mp4.jpg', 'v0200f950000bg19ilkr08mdrh4kblhg.mp4.jpg', 'v0200f9a0000bbninp7ijqt2hsvv1ktg.mp4.jpg', 'v0200f9a0000bckfti5ahtmckcqjvoqg.mp4.jpg', 'v0200f9a0000bcl79ga7u0r58fp0entg.mp4.jpg', 'v0200f9a0000bddhq1l81shglr35iesg.mp4.jpg', 'v0200f9a0000bdfv1cl81shglr3b0nq0.mp4.jpg', 'v0200f9a0000bdpnpdnijqt2hsv3jb10.mp4.jpg', 'v0200f9a0000belo1mqepr1549mon5b0.mp4.jpg', 'v0200f9b0000bfe3qbdjfrmg0k8hdci0.mp4.jpg', 'v0200f9b0000bfe40hsmavf2i72k9410.mp4.jpg', 'v0200fa20000beedmtd1mik483s3pra0.mp4.jpg', 'v0200fa50000bbk1o7r6936njil2d3sg.mp4.jpg', 'v0200fa80000bds1snmdm152mr3h46t0.mp4.jpg', 'v0200fa90000beeuvstahtmapjmbfk60.mp4.jpg', 'v0200fab0000bbigv1jcp2339jnq25q0.mp4.jpg', 'v0200fab0000bbk1oit7gl1g0j0c07pg.mp4.jpg', 'v0200fac0000bcire1o697aveh0j7n40.mp4.jpg', 'v0200fad0000bemcll0a2pemnbc8hg1g.mp4.jpg', 'v0200fb00000bbjj7shdli3g7cn3v470.mp4.jpg', 'v0200fb00000bbjj95onrm1o4bb5fnag.mp4.jpg', 'v0200fb30000bblf7c6j5ugsaq9sng90.mp4.jpg', 'v0200fb80000bd9l04cuatl9jve92t70.mp4.jpg', 'v0200fbb0000bcfposrbo1i42cr54b80.mp4.jpg', 'v0200fbb0000bcfpq2agd9frq74e6fgg.mp4.jpg', 'v0200fbc0000bc5k1fr82vu4lfmg9rjg.mp4.jpg', 'v0200fbc0000bc9u0ivrri6cjko30h10.mp4.jpg', 'v0200fbd0000bc2ppuceae1bqn8tosog.mp4.jpg', 'v0200fbd0000bck8t5cthbi90j16h5ag.mp4.jpg', 'v0200fbd0000bcmu78ir863ntv7s4kug.mp4.jpg', 'v0200fbd0000bcpntlqr863ntv036odg.mp4.jpg', 'v0200fbd0000bd1k9sij2boojm7b65kg.mp4.jpg', 'v0200fbd0000bd3gkj4eae1bqnckcqjg.mp4.jpg', 'v0200fbd0000bdchohmj5ugob88s2kmg.mp4.jpg', 'v0200fbd0000bdes4sij2boojm0abeqg.mp4.jpg', 'v0200fc10000bep25bl1mik75275urmg.mp4.jpg', 'v0200fc10000beq9uhs81ukv9hto28o0.mp4.jpg', 'v0200fc10000bes9gee4tqbmgbr0th5g.mp4.jpg', 'v0200fc20000bbu5rdjbo1id4cj4jqo0.mp4.jpg', 'v0200fc20000bdddhprbo1id4cgekmug.mp4.jpg', 'v0200fc20000bdpq90pq4do2tlmejopg.mp4.jpg', 'v0200fc20000bdqe3c9q4do2tlmga3ag.mp4.jpg', 'v0200fc50000becs7j57gl1ihk0jd3ig.mp4.jpg', 'v0200fc50000bef35j0ckqbk6j23skag.mp4.jpg', 'v0200fce0000beh2cdqikato7dhbmbdg.mp4.jpg', 'v0200fd10000beiphdkthbi68g90asc0.mp4.jpg', 'v0200fdc0000be5s5nm8qbl0p3iarjlg.mp4.jpg', 'v0200fdf0000bfh41127u0r6u32kbung.mp4.jpg', 'v0200fe20000be1k88a0ifkuiknvalk0.mp4.jpg', 'v0200fe70000bbm892mbm86jq9v1dang.mp4.jpg', 'v0200fe70000bcmee26bm86jq9pvj6qg.mp4.jpg', 'v0200fe70000bcoeqatds13bnrvdiasg.mp4.jpg', 'v0200fe70000bda5puo697asd609aec0.mp4.jpg', 'v0200fe70000bdpvg61pjc2vij6mnqeg.mp4.jpg', 'v0200ff00000bddgs6viv420lsv0lr80.mp4.jpg', 'v0200ff00000bdpadnf2gddrulr45sag.mp4.jpg', 'v0200ff20000bceg6og9lr76j640ig8g.mp4.jpg', 'v0200ff50000bblrfmoghl0mbk8pc1o0.mp4.jpg', 'v0200ff50000bboru1jc86dlg7h936h0.mp4.jpg', 'v0200ff50000bbsrco3c86dlg7hkv350.mp4.jpg', 'v0200ff50000bc5vtneue3mhdhdlldqg.mp4.jpg', 'v0200ff50000bc6e7ho858lvukqku760.mp4.jpg', 'v0200ff50000bcfnumockqbl35lq81hg.mp4.jpg', 'v0200ff50000bcvmgn8ckqbl35n3p5jg.mp4.jpg', 'v0200ff50000bd4bmu6dm155hh1nhh30.mp4.jpg', 'v0200ff50000bd5htsr6j2qh9hfosjog.mp4.jpg', 'v0200ff50000bd8upga0ifkv1vh01a8g.mp4.jpg', 'v0200ff50000bd9i2bfa1hap4advedp0.mp4.jpg', 'v0200ff70000bbs73b2k781i9vlee4d0.mp4.jpg', 'v0200ff70000bc4ofad34q13tigivqjg.mp4.jpg', 'v0200ff70000bc8lj4ugnco3genh72sg.mp4.jpg', 'v0200ff70000bcifealjfrmnl4rl9kdg.mp4.jpg', 'v0200ff70000bd7av5mgnco3gei06sg0.mp4.jpg', 'v0200ff70000bdfgdj1dli3m0gpmpgqg.mp4.jpg', 'v0200ff70000bdpdbismavf9lstim2v0.mp4.jpg', 'v0200ffd0000bdtn07d8n75p2eok09p0.mp4.jpg', 'v0200fff0000bdrus2fm1hfcc2ndh3kg.mp4.jpg', 'v0200fff0000bemv1ftds139ik9qabi0.mp4.jpg', 'v0300f4a0000bfaq291sm3ih2a9vhjj0.mp4.jpg', 'v0300f600000bfmk419sm3iq9odf5t10.mp4.jpg', 'v0300f6c0000bdko8r5ehji8icg3nkd0.mp4.jpg', 'v0300f900000bfn3dskhpahnp1kr7tog.mp4.jpg', 'v0300f930000bev8il8e8b7r0uejkk00.mp4.jpg', 'v0300f9a0000bemdkmcqn5hfpb78jukg.mp4.jpg', 'v0300f9a0000benl44lm7i9j7fe5c0mg.mp4.jpg', 'v0300f9a0000bennvv1sm3ighmfmang0.mp4.jpg']
for i in setlist:
    w.write(i+'\n')
kj=open('E:/pic/111/picture/2018/12/bb.txt','w')
kj.write(w.getvalue())





print(listcontain)
print(len(listcontain))