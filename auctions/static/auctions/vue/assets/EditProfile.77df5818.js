import{d as h,_ as g,r as f,o as r,c as d,a as i,t as m,f as c,v as u,b as y,w as b}from"./index.ed948278.js";const _=h({data(){return{id:0,name:"",city:"",dob:"",email:"",dp:"",image:void 0}},components:{},methods:{async update_user(){let e=document.getElementById("put"),t=document.getElementById("e_mail").value,a=document.getElementById("city").value,s=document.getElementById("dob").value,n=document.getElementById("image").value;if(!(o=>String(o).toLowerCase().match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/))(t)){alert("Please enter a valid email");return}if(t==""&&a==""&&!s&&!n){alert("Please enter details");return}if(t==""){alert("Please enter an email");return}if(a==""){alert("Please enter a city");return}if(!s){alert("Please enter a date of birth");return}if(!n){alert("Please upload an image");return}let l="http://127.0.0.1:8000/api/users/";if(e){const o=new FormData(e);o.append("id",this.id.toString()),this.image&&(o.append("profile_picture",this.image),console.log(1)),await fetch(l,{method:"PUT",body:o,headers:{"X-CSRFToken":this.getCookie()}}),window.location.replace("http://127.0.0.1:8000/profile")}},async get_id(){let t=await(await fetch("http://127.0.0.1:8000/api/uid/",{method:"GET"})).json();this.id=t.id,this.fetch_user()},async fetch_user(){let e="http://127.0.0.1:8000/api/user/"+this.id+"/",a=await(await fetch(e,{method:"GET"})).json();console.log(a.user[0]),this.city=a.user[0].city,this.dob=a.user[0].dob,this.email=a.user[0].email,this.dp=a.user[0].profile_picture},getCookie(){let e="";if(document.cookie&&document.cookie!=="")for(var t=document.cookie.split(";"),a=0;a<t.length;a++){var s=t[a].trim();if(s.substring(0,10)==="csrftoken="){e=decodeURIComponent(s.substring(10));break}}return e},changeImage(){let e=document.getElementById("image");this.image=e}},mounted(){this.get_id()}}),v={class:"container mt-4"},w={class:"row"},E={class:"col-sm-2 text-center mb-2"},k=["src"],C=["src"],B={class:"col-sm-8 text-center p-2 rounded",style:{"background-color":"rgb(23,45,125,0.2)"}},I={id:"put"},P={class:"text-secondary mt-3 mb-1"},U={class:"text-secondary mt-3 mb-1"},V=i("p",{class:"text-secondary mt-3 mb-1"},"Upload profile picture",-1),$={class:"col-sm-2 text-center"},T=i("button",{class:"btn btn-primary"},"View profile",-1),x={class:"text-center"};function D(e,t,a,s,n,p){const l=f("router-link");return r(),d("div",v,[i("div",w,[i("div",E,[e.dp!=""?(r(),d("img",{key:0,src:"http://127.0.0.1:8000/media/"+e.dp,style:{width:"5em",height:"5em"}},null,8,k)):(r(),d("img",{key:1,src:"http://127.0.0.1:8000/media/default_profile_picture.png",style:{width:"5em",height:"5em"}},null,8,C))]),i("div",B,[i("form",I,[i("h1",null,"Email: "+m(e.email),1),c(i("input",{class:"input-group mx-auto text-center",name:"email",id:"e_mail",style:{width:"60%"},"onUpdate:modelValue":t[0]||(t[0]=o=>e.email=o),placeholder:"Enter email"},null,512),[[u,e.email]]),i("p",P,"City: "+m(e.city),1),c(i("input",{class:"input-group mx-auto text-center",name:"city",id:"city",style:{width:"60%"},"onUpdate:modelValue":t[1]||(t[1]=o=>e.city=o),placeholder:"Enter city"},null,512),[[u,e.city]]),i("p",U,"Date of birth: "+m(e.dob),1),c(i("input",{class:"input-group mx-auto text-center",name:"dob",id:"dob",style:{width:"60%"},"onUpdate:modelValue":t[2]||(t[2]=o=>e.dob=o),placeholder:"Enter dob"},null,512),[[u,e.dob]]),V,i("input",{type:"file",name:"image",class:"form-control",accept:"image/*",onChange:t[3]||(t[3]=o=>e.changeImage()),id:"image"},null,32)])]),i("div",$,[y(l,{to:"/profile"},{default:b(()=>[T]),_:1})])]),i("div",x,[i("button",{class:"btn btn-primary mt-3",onClick:t[4]||(t[4]=(...o)=>e.update_user&&e.update_user(...o))},"Update")])])}const j=g(_,[["render",D]]);export{j as default};
