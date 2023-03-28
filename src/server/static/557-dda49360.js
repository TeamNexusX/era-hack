"use strict";(self.webpackChunkdashboard_62=self.webpackChunkdashboard_62||[]).push([[557],{7557:(e,n,r)=>{r.r(n),r.d(n,{default:()=>B});var a=r(5893),t=r(4807),i=r(2594),l=r(7294),s=r(2012),o=r(4184),d=r.n(o),c=r(6792),u=r(3439);function f(e,n,r){const a=(e-n)/(r-n)*100;return Math.round(1e3*a)/1e3}function v({min:e,now:n,max:r,label:t,visuallyHidden:i,striped:l,animated:s,className:o,style:c,variant:u,bsPrefix:v,...p},h){return(0,a.jsx)("div",{ref:h,...p,role:"progressbar",className:d()(o,`${v}-bar`,{[`bg-${u}`]:u,[`${v}-bar-animated`]:s,[`${v}-bar-striped`]:s||l}),style:{width:`${f(n,e,r)}%`,...c},"aria-valuenow":n,"aria-valuemin":e,"aria-valuemax":r,children:i?(0,a.jsx)("span",{className:"visually-hidden",children:t}):t})}const p=l.forwardRef((({isChild:e,...n},r)=>{if(n.bsPrefix=(0,c.vE)(n.bsPrefix,"progress"),e)return v(n,r);const{min:t,now:i,max:s,label:o,visuallyHidden:f,striped:p,animated:h,bsPrefix:m,variant:b,className:x,children:y,...g}=n;return(0,a.jsx)("div",{ref:r,...g,className:d()(x,m),children:y?(0,u.UI)(y,(e=>(0,l.cloneElement)(e,{isChild:!0}))):v({min:t,now:i,max:s,label:o,visuallyHidden:f,striped:p,animated:h,bsPrefix:m,variant:b},r)})}));p.displayName="ProgressBar",p.defaultProps={min:0,max:100,animated:!1,isChild:!1,visuallyHidden:!1,striped:!1};const h=p;var m=r(8375),b=r(5005),x=r(7440),y=r(2672),g=r(9704),w=r(6088),j=r(9250),Z=function(e){var n;return null===(n=e.filesUpload)||void 0===n?void 0:n.isLoading},k=function(e){var n;return null===(n=e.filesUpload)||void 0===n?void 0:n.error},P=function(e){var n;return(null===(n=e.filesUpload)||void 0===n?void 0:n.currentlyUploaded)||0},N=function(e){var n;return(null===(n=e.filesUpload)||void 0===n?void 0:n.totalFileSize)||1},C=r(5999),S=r(3379),T=r.n(S),U=r(7795),F=r.n(U),H=r(569),I=r.n(H),$=r(3565),A=r.n($),E=r(9216),O=r.n(E),z=r(4589),D=r.n(z),G=r(2322),L={};L.styleTagTransform=D(),L.setAttributes=A(),L.insert=I().bind(null,"head"),L.domAPI=F(),L.insertStyleElement=O(),T()(G.Z,L);const q=G.Z&&G.Z.locals?G.Z.locals:void 0;var Q=r(6105),R=function(){return R=Object.assign||function(e){for(var n,r=1,a=arguments.length;r<a;r++)for(var t in n=arguments[r])Object.prototype.hasOwnProperty.call(n,t)&&(e[t]=n[t]);return e},R.apply(this,arguments)},_={filesUpload:C.Oe};const B=(0,l.memo)((function(e){var n=e.className,r=(0,x.Fg)().theme,o=(0,j.s0)(),d=(0,g.v9)(k),c=(0,g.v9)(Z),u=(0,g.v9)(P),f=(0,g.v9)(N),v=(0,y.T)(),p=(0,l.useState)(!1),C=p[0],S=p[1],T=(0,l.useState)(""),U=T[0],F=T[1],H=(0,l.useCallback)((function(e){return n=void 0,r=void 0,t=function(){var n,r,a,t,i;return function(e,n){var r,a,t,i,l={label:0,sent:function(){if(1&t[0])throw t[1];return t[1]},trys:[],ops:[]};return i={next:s(0),throw:s(1),return:s(2)},"function"==typeof Symbol&&(i[Symbol.iterator]=function(){return this}),i;function s(s){return function(o){return function(s){if(r)throw new TypeError("Generator is already executing.");for(;i&&(i=0,s[0]&&(l=0)),l;)try{if(r=1,a&&(t=2&s[0]?a.return:s[0]?a.throw||((t=a.return)&&t.call(a),0):a.next)&&!(t=t.call(a,s[1])).done)return t;switch(a=0,t&&(s=[2&s[0],t.value]),s[0]){case 0:case 1:t=s;break;case 4:return l.label++,{value:s[1],done:!1};case 5:l.label++,a=s[1],s=[0];continue;case 7:s=l.ops.pop(),l.trys.pop();continue;default:if(!((t=(t=l.trys).length>0&&t[t.length-1])||6!==s[0]&&2!==s[0])){l=0;continue}if(3===s[0]&&(!t||s[1]>t[0]&&s[1]<t[3])){l.label=s[1];break}if(6===s[0]&&l.label<t[1]){l.label=t[1],t=s;break}if(t&&l.label<t[2]){l.label=t[2],l.ops.push(s);break}t[2]&&l.ops.pop(),l.trys.pop();continue}s=n.call(e,l)}catch(e){s=[6,e],a=0}finally{r=t=0}if(5&s[0])throw s[1];return{value:s[0]?s[1]:void 0,done:!0}}([s,o])}}}(this,(function(l){switch(l.label){case 0:return e.preventDefault(),n=new FormData(e.currentTarget),[4,v((0,Q.I)(n))];case 1:return"fulfilled"===(r=l.sent()).meta.requestStatus&&(S(!0),(null===(t=null===(a=null==r?void 0:r.payload)||void 0===a?void 0:a.message)||void 0===t?void 0:t.includes("существуют"))&&F(null===(i=null==r?void 0:r.payload)||void 0===i?void 0:i.message)),[2]}}))},new((a=void 0)||(a=Promise))((function(e,i){function l(e){try{o(t.next(e))}catch(e){i(e)}}function s(e){try{o(t.throw(e))}catch(e){i(e)}}function o(n){var r;n.done?e(n.value):(r=n.value,r instanceof a?r:new a((function(e){e(r)}))).then(l,s)}o((t=t.apply(n,r||[])).next())}));var n,r,a,t}),[v]);return(0,a.jsx)(w.W,R({reducers:_},{children:(0,a.jsx)(i.T,R({className:(0,t.A)(q.UploadFilesPage,{},[n])},{children:(0,a.jsxs)(s.Z,R({onSubmit:H,encType:"multipart/form-data"},{children:[(0,a.jsx)("h2",{children:"Загрузка новых данных о кандидатах"}),(0,a.jsxs)(s.Z.Group,R({controlId:"formFile",className:"mb-3"},{children:[(0,a.jsx)(s.Z.Label,{children:"Выберите архив с анкетами."}),(0,a.jsx)(s.Z.Control,{disabled:c,id:"files",name:"files",required:!0,accept:".zip,.rar,.7z",type:"file"})]})),c&&(0,a.jsx)(h,{className:q.progress,animated:!0,variant:"success",label:"".concat((u/f*100).toFixed(2),"%"),now:u/f*100}),d&&(0,a.jsx)(m.Z,R({variant:"danger"},{children:d})),C&&(0,a.jsxs)(m.Z,R({variant:U?"warning":"success"},{children:[U?(0,a.jsx)("p",{children:U}):(0,a.jsx)("p",{children:"Все анкеты успешно добавлены"}),(0,a.jsx)(b.Z,R({variant:r===x.Q2.LIGHT?"success":"success-dark",onClick:function(){return o("/candidates")}},{children:"Перейти на страницу сравнения"}))]})),!c&&!C&&(0,a.jsx)(b.Z,R({disabled:c,type:"submit",variant:r===x.Q2.DARK?"info":"dark"},{children:"Отправить анкеты"}))]}))}))}))}))},2322:(e,n,r)=>{r.d(n,{Z:()=>s});var a=r(8081),t=r.n(a),i=r(3645),l=r.n(i)()(t());l.push([e.id,"*{text-align:left}.dbe75{height:35px;margin-bottom:15px}",""]),l.locals={progress:"dbe75"};const s=l}}]);