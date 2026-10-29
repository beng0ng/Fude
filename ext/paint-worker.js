
// Everything between these markers is pure: no DOM, no outer variables. It runs on the main thread,
// and the same text is loaded into a Web Worker so painting never stalls the page.
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function makeNoise(seed){
  const r=mulberry32(seed),p=new Uint8Array(512),gx=new Float32Array(256),gy=new Float32Array(256);
  const perm=[...Array(256).keys()];for(let i=255;i>0;i--){const j=Math.floor(r()*(i+1));[perm[i],perm[j]]=[perm[j],perm[i]]}
  for(let i=0;i<512;i++)p[i]=perm[i&255];for(let i=0;i<256;i++){const a=r()*Math.PI*2;gx[i]=Math.cos(a);gy[i]=Math.sin(a)}
  const fade=t=>t*t*t*(t*(t*6-15)+10);
  const n=(x,y)=>{const xi=Math.floor(x),yi=Math.floor(y),xf=x-xi,yf=y-yi,X=xi&255,Y=yi&255;
    const g=(h,dx,dy)=>gx[h]*dx+gy[h]*dy;
    const aa=p[p[X]+Y],ab=p[p[X]+Y+1],ba=p[p[X+1]+Y],bb=p[p[X+1]+Y+1];
    const u=fade(xf),v=fade(yf);
    const x1=g(aa,xf,yf)+u*(g(ba,xf-1,yf)-g(aa,xf,yf)),x2=g(ab,xf,yf-1)+u*(g(bb,xf-1,yf-1)-g(ab,xf,yf-1));
    return (x1+v*(x2-x1))*1.4};
  n.fbm=(x,y,o=4)=>{let s=0,a=.5,f=1;for(let i=0;i<o;i++){s+=a*n(x*f,y*f);f*=2.02;a*=.5}return s};
  return n;
}
const clampF=(v,a,b)=>v<a?a:v>b?b:v;
// every pixel joins a band by the rank of its field value, so each color gets its exact share
function assign(field,bands){
  const N=field.length,B=16384;let mn=Infinity,mx=-Infinity;
  for(let i=0;i<N;i++){const v=field[i];if(v<mn)mn=v;if(v>mx)mx=v}
  const sc=(B-1)/((mx-mn)||1),bin=new Uint16Array(N),hist=new Uint32Array(B);
  for(let i=0;i<N;i++){const k=((field[i]-mn)*sc)|0;bin[i]=k;hist[k]++}
  const start=new Uint32Array(B);let acc=0;for(let k=0;k<B;k++){start[k]=acc;acc+=hist[k]}
  const tw=bands.reduce((a,b)=>a+b.w,0),cut=[];let c=0;bands.forEach(b=>{c+=b.w/tw;cut.push(Math.round(c*N))});cut[cut.length-1]=N;
  const bandOfRank=new Uint8Array(N),bandStart=[0,...cut.slice(0,-1)];
  for(let j=0,r=0;j<cut.length;j++)for(;r<cut[j];r++)bandOfRank[r]=j;
  const out=new Uint8Array(N),t=new Float32Array(N),counter=new Uint32Array(B),counts=new Array(bands.length).fill(0);
  for(let i=0;i<N;i++){const k=bin[i],rank=start[k]+counter[k]++;const j=bandOfRank[rank];out[i]=j;counts[j]++;
    const s=bandStart[j],len=cut[j]-s;t[i]=len>1?(rank-s)/(len-1):.5}
  return{band:out,t,counts};
}
function shadeTo(c,s,l=255){return s<0?c+s*c:c+s*(l-c)}
// the field: for a painting, its blurred luminance; for a theme, a procedural landscape
function genField(kind,id,seed,size,params,lumArr,W,H){
  const p=Object.assign({scale:1,warp:.5,focusX:.5,focusY:.5},params||{});let field;
  if(kind==='painting'){
    field=new Float32Array(W*H);const r=mulberry32(seed);
    // a light blur keeps regions whole instead of speckled; detail returns in the shading
    const tmp=new Float32Array(W*H),R2=Math.max(2,Math.round(2*Math.sqrt(Math.max(W,H)/640)));
    for(let y=0;y<H;y++){let acc=0,c=0;for(let x=-R2;x<W;x++){if(x+R2<W){acc+=lumArr[y*W+x+R2];c++}if(x-R2-1>=0){acc-=lumArr[y*W+x-R2-1];c--}if(x>=0)tmp[y*W+x]=acc/c}}
    for(let x=0;x<W;x++){let acc=0,c=0;for(let y=-R2;y<H;y++){if(y+R2<H){acc+=tmp[(y+R2)*W+x];c++}if(y-R2-1>=0){acc-=tmp[(y-R2-1)*W+x];c--}if(y>=0)field[y*W+x]=acc/c}}
    // edge-aware smoothing: light flows between neighbours of similar brightness but not across a contour, so the bands follow the painting's shapes
    const K2=.0036,lam=.22;
    for(let it=0;it<7;it++){tmp.set(field);
      for(let y=1;y<H-1;y++)for(let x=1;x<W-1;x++){const i=y*W+x,v=tmp[i];let acc=0;
        const dn=tmp[i-W]-v,ds=tmp[i+W]-v,de=tmp[i+1]-v,dw=tmp[i-1]-v;
        acc+=dn/(1+dn*dn/K2)+ds/(1+ds*ds/K2)+de/(1+de*de/K2)+dw/(1+dw*dw/K2);field[i]=v+lam*acc}}
    for(let i=0;i<W*H;i++)field[i]+=(r()-.5)*.002;
  }else{
    W=H=size||640;field=new Float32Array(W*H);lumArr=null;const n=makeNoise(seed),r=mulberry32(seed+3),s=p.scale,wp=p.warp;
    let stones=[];
    if(id==='sand'){const k=2+Math.floor(r()*2);for(let i=0;i<k;i++)stones.push({x:clampF(p.focusX+(r()-.5)*.6,.15,.85),y:clampF(p.focusY+(r()-.5)*.5,.18,.82),R:.04+r()*.05})}
    const tiles=24,tileJ=new Float32Array(tiles*tiles).map(()=>r());
    for(let y=0;y<H;y++){const v=y/H;for(let x=0;x<W;x++){const u=x/W;let f;
      if(id==='enso'){const dx=u-p.focusX,dy=v-p.focusY,d=Math.sqrt(dx*dx+dy*dy),a=Math.atan2(dy,dx);
        f=d+.045*wp*n.fbm(Math.cos(a)*1.3*s+3,Math.sin(a)*1.3*s+3,3)+.012*n(a*7,d*3)+.004*n(a*60,d*80)}
      else if(id==='sand'){f=v+.012*Math.sin(u*Math.PI*2*s+seed)+.01*wp*n(u*2,v*2);
        for(const st of stones){const dx=u-st.x,dy=(v-st.y),d=Math.sqrt(dx*dx+dy*dy);
          if(d<st.R){f=-1+d;break}const w=clampF((st.R*3-d)/(st.R*1.6),0,1);const ring=st.y-st.R*.4+(d-st.R)*.9;f=f*(1-w)+ring*w}}
      else if(id==='marble'){const q1=n.fbm(u*2*s,v*2*s),q2=n.fbm(u*2*s+5.2,v*2*s+1.3);f=n.fbm(u*2*s+3.5*wp*q1,v*2*s+3.5*wp*q2,5)}
      else if(id==='field'){f=v+.03*n.fbm(u*2.5*s,v*2.5*s,3)+.006*n(u*30,v*30)}
      else if(id==='topo'){f=n.fbm(u*2.4*s+wp*.4*n(u*3,v*3),v*2.4*s,5)}
      else{const ti=Math.min(tiles-1,(u*tiles)|0),tj=Math.min(tiles-1,(v*tiles)|0);f=n.fbm(ti/tiles*2.2*s,tj/tiles*2.2*s,3)+.08*wp*tileJ[tj*tiles+ti]+(((v*tiles)%1)*.0001)}
      field[y*W+x]=f}}
  }
  return{W,H,field,lumArr};
}
// color every pixel: its band's color, shaded by the painting's light or the theme's texture
function shadePixels(m,F){
  const {W,H,field,lumArr}=F,bands=m.bands,rgbs=m.rgbs,id=m.id,tiles=24;
  const {band,t,counts}=assign(field,bands),light=m.light||[255,255,255],sk=Math.pow(Math.max(W,H)/640,.6); // the highlights take the color of the song's key; sk keeps the strokes in proportion at any size
  const d=new Uint8ClampedArray(W*H*4),g=mulberry32(m.seed+11),bn=lumArr?makeNoise(m.seed+5):null;
  let meanL=null;
  if(lumArr){const sum=new Float64Array(bands.length);for(let i=0;i<W*H;i++)sum[band[i]]+=lumArr[i];meanL=[...sum].map((v,j)=>v/(counts[j]||1))}
  for(let i=0;i<W*H;i++){
    const j=band[i],c=rgbs[j];let s=0;
    if(lumArr){s=(lumArr[i]-meanL[j])*1.15;
      // brush strokes: faint ridges that run along the contours of the painting, in the direction of its shapes
      const x=i%W,y=(i/W)|0;let gx=.707,gy=.707;
      if(x>0&&x<W-1&&y>0&&y<H-1){const ex=field[i+1]-field[i-1],ey=field[i+W]-field[i-W],mg=Math.sqrt(ex*ex+ey*ey);if(mg>1e-4){const wgt=clampF(mg*30,0,1);gx=(ex/mg)*wgt+.707*(1-wgt);gy=(ey/mg)*wgt+.707*(1-wgt)}}
      const ph=(x*gx+y*gy)*1.05/sk+bn(x*.028/sk,y*.028/sk)*5.5;s+=.04*Math.sin(ph)*(.65+.35*Math.sin(ph*.41+1.3))}
    else{
      const ti=t[i];
      if(id==='field')s=-.16*(1-Math.sin(Math.PI*ti))+.04;
      else s=(ti-.5)*.1;
      if(id==='sand')s+=.07*Math.sin(field[i]*Math.PI*2*70);
      if(id==='topo'){const cfr=(field[i]*26)%1;if(cfr<.05||cfr>.97)s-=.14}
      if(id==='marble'&&(ti<.035||ti>.965))s-=.18;
      if(id==='enso')s+=.05*Math.sin(field[i]*Math.PI*2*55);
      if(id==='mosaic'){const x=i%W,y=(i/W)|0,lu=(x/W*tiles)%1,lv=(y/H*tiles)%1;if(lu<.07||lv<.07)s-=.22;else if(lu>.93||lv>.93)s+=.06}
      s+=(g()-.5)*.03;
    }
    const k=i*4;d[k]=shadeTo(c[0],s,light[0]);d[k+1]=shadeTo(c[1],s,light[1]);d[k+2]=shadeTo(c[2],s,light[2]);d[k+3]=255;
  }
  return{buf:d,counts,W,H};
}

const fields=new Map(),lums=new Map();
onmessage=e=>{const m=e.data;try{
  if(m.lumArr)lums.set(m.id,{W:m.W,H:m.H,lumArr:m.lumArr});
  let F=fields.get(m.fieldKey);
  if(!F){const L=m.kind==='painting'?lums.get(m.id):null;if(m.kind==='painting'&&!L){postMessage({job:m.job,needLum:true});return}
    F=genField(m.kind,m.id,m.seed,m.size,m.params,L&&L.lumArr,L&&L.W,L&&L.H);fields.set(m.fieldKey,F);if(fields.size>3)fields.delete(fields.keys().next().value)}
  const r=shadePixels(m,F);postMessage({job:m.job,buf:r.buf,W:r.W,H:r.H,counts:r.counts},[r.buf.buffer]);
}catch(err){postMessage({job:m.job,error:String(err&&err.message||err)})}};