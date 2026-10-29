
function vRand(seed){let a=seed>>>0;return()=>{a=(a+0x6D2B79F5)>>>0;let t=a;t=Math.imul(t^(t>>>15),t|1);t^=t+Math.imul(t^(t>>>7),t|61);return((t^(t>>>14))>>>0)/4294967296}}
function vFreq(m){return 440*Math.pow(2,(m-69)/12)}
// sum of decaying sine partials; each has a slow decay (a, tau) and an optional prompt decay (a2, tau2)
function vPartials(out,sr,parts){const n=out.length,TAU=6.283185307179586;
  for(const p of parts){if(p.f>=sr*.47)continue;const w=TAU*p.f/sr,d1=Math.exp(-1/(p.tau*sr)),d2=p.tau2?Math.exp(-1/(p.tau2*sr)):0,att=Math.max(1,Math.round((p.att||0)*sr));let ph=p.ph||0,e1=p.a,e2=p.a2||0;
    for(let i=0;i<n;i++){const env=(e1+e2)*(i<att?i/att:1);out[i]+=env*Math.sin(ph);ph+=w;if(ph>TAU)ph-=TAU;e1*=d1;e2*=d2;if(e1+e2<1e-5)break}}}
// a short burst of lowpassed noise: hammer, mallet or pluck
function vThump(out,sr,amp,secs,cut,seed){const r=vRand(seed);let lp=0;const c=Math.min(1,cut/sr*6.28),n=Math.min(out.length,Math.round(secs*5*sr));for(let i=0;i<n;i++){lp+=((r()*2-1)-lp)*c;out[i]+=lp*amp*Math.exp(-i/(secs*sr))}}
function vPiano(midi,sr,out){const f0=vFreq(midi),t=Math.max(0,Math.min(1,(midi-48)/40)),B=.00012+.0009*t,bright=Math.max(0,Math.min(1,(midi-30)/60));
  const tau=Math.max(.45,Math.min(5,4.2*Math.pow(2,-(midi-48)/22))),parts=[],N=Math.min(14,Math.floor(sr*.46/f0)),strings=midi<36?1:midi<52?2:3;
  for(let k=1;k<=N;k++){const fk=k*f0*Math.sqrt(1+B*k*k),hammer=Math.abs(Math.sin(Math.PI*k/7.3))+.08;let a=Math.pow(k,-1.25)*hammer*(k===1?1:.85);a*=1/(1+Math.pow(fk/(2600+3200*bright),2));
    const tk=tau/(1+.09*k*k)+.01,tf=Math.min(tk,.35/(1+.2*k));
    for(let s=0;s<strings;s++){const det=strings===1?0:(s-(strings-1)/2)*(.0007+.0004*bright);parts.push({f:fk*(1+det),a:a*.55/strings,tau:tk,a2:a*.45/strings,tau2:tf,ph:(k*1.7+s)%6.28,att:.0025})}}
  vPartials(out,sr,parts);vThump(out,sr,.22*(1-.4*bright),.006,3500+3000*bright,midi*7+1);vThump(out,sr,.05,.03,260,midi*3+9)}
// Karplus-Strong plucked string with a fractional delay, a pluck-position comb and a target decay time
function vString(midi,sr,out,o){const f0=vFreq(midi),N=sr/f0-.5,L=Math.ceil(N)+3,buf=new Float32Array(L),ex=new Float32Array(L),r=vRand(midi*13+5),g=Math.pow(10,-3/(o.t60*sr)),bright=o.bright;
  let lp=0;for(let i=0;i<L;i++){lp+=((r()*2-1)-lp)*bright;ex[i]=lp}const pp=Math.max(1,Math.round(L*o.pos));for(let i=0;i<L;i++)buf[i]=ex[i]-(i>=pp?ex[i-pp]:0)*.9;
  let w=0,last=0;const n=out.length;for(let i=0;i<n;i++){const rd=w-N;let ri=Math.floor(rd);const fr=rd-ri;ri=((ri%L)+L)%L;const x=buf[ri]*(1-fr)+buf[(ri+1)%L]*fr,y=(x+last)*.5*g;last=x;buf[w]=y;w=(w+1)%L;out[i]+=y*o.amp}}
function vHarp(midi,sr,out){const t60=Math.max(.9,Math.min(4,3*Math.pow(2,-(midi-50)/20)));vString(midi,sr,out,{t60,bright:.3+.55*Math.max(0,Math.min(1,(midi-40)/50)),pos:.22,amp:.6});vThump(out,sr,.06,.002,5000,midi*5+1)}
function vMusicbox(midi,sr,out){const f0=vFreq(midi+12),tau=Math.max(.5,Math.min(2.2,2*Math.pow(2,-(midi-60)/18)));
  vPartials(out,sr,[{f:f0,a:.7,tau,att:.001},{f:f0*6.27,a:.12,tau:tau*.12,att:.001},{f:f0*17.55,a:.04,tau:tau*.05,att:.001},{f:f0*2.01,a:.05,tau:tau*.4}]);vThump(out,sr,.15,.002,6000,midi*5+3)}
function vMarimba(midi,sr,out){const f0=vFreq(midi),tau=Math.max(.18,Math.min(1.1,.9*Math.pow(2,-(midi-55)/14)));
  vPartials(out,sr,[{f:f0,a:.8,tau,att:.004},{f:f0*3.93,a:.35,tau:tau*.22,att:.002},{f:f0*9.54,a:.12,tau:tau*.08,att:.001}]);vThump(out,sr,.25,.003,2500,midi*11+2)}
const VOICE_LEN={piano:m=>Math.max(.9,3.6*Math.pow(2,-(m-48)/22)),harp:m=>Math.max(1,3.3*Math.pow(2,-(m-50)/20)),musicbox:m=>Math.max(.7,2.3*Math.pow(2,-(m-60)/18)),marimba:m=>Math.max(.3,1.2*Math.pow(2,-(m-55)/14))};
function renderVoice(inst,midi,sr,maxLen){const secs=Math.min(maxLen,VOICE_LEN[inst](midi)),out=new Float32Array(Math.ceil(secs*sr));
  if(inst==='piano')vPiano(midi,sr,out);else if(inst==='harp')vHarp(midi,sr,out);else if(inst==='musicbox')vMusicbox(midi,sr,out);else vMarimba(midi,sr,out);
  let pk=0;for(let i=0;i<out.length;i++){const v=Math.abs(out[i]);if(v>pk)pk=v}if(pk>0){const s=.9/pk;for(let i=0;i<out.length;i++)out[i]*=s}
  const fade=Math.min(out.length,Math.round(sr*.3));for(let i=0;i<fade;i++)out[out.length-1-i]*=i/fade;
  return out}

self.onmessage=e=>{const {inst,midi,sr,max}=e.data;const d=renderVoice(inst,midi,sr,max);self.postMessage({inst,midi,sr,d},[d.buffer])};