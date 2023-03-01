import{d as u,_ as p,r as f,o as y,c as g,a as e,f as n,v as i,g as h,b as _,w as b}from"./index.ed948278.js";const w=u({data(){return{users:[],image:void 0,email:"",password:"",dob:"",city:""}},components:{},methods:{async get_csrf(){await(await fetch("http://127.0.0.1:8000/login/",{method:"GET"})).text()},async get_users(){let o=await(await fetch("http://127.0.0.1:8000/api/users/",{method:"GET"})).json();this.users=o.users},async add_user(){let t=document.getElementById("post"),o=document.getElementById("typeEmailX").value,r=document.getElementById("typePasswordX").value,a=document.getElementById("typeDateX").value,d=document.getElementById("typeCityX").value,c=document.getElementById("typeImageX").value;if(!(l=>String(l).toLowerCase().match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/))(o)){alert("Please enter a valid email");return}if(o==""&&r==""&&!a&&d==""&&!c){alert("Please enter your details");return}if(o==""){alert("Please enter your email");return}if(r==""){alert("Please enter your password");return}if(d==""){alert("Please enter your city");return}if(!c){alert("Please add your profile image");return}let s=new Date;if(a>s.toISOString()){alert("Please enter a past date");return}if(a>new Date){alert("Please enter a valid date");return}if(!a){alert("Please enter your date");return}if(t){const l=new FormData(t);this.image&&l.append("picture",this.image),await fetch("http://127.0.0.1:8000/api/users/",{method:"POST",body:l,headers:{"X-CSRFToken":this.getCookie()}}),window.location.replace("http://127.0.0.1:8000")}this.get_users()},changeImage(){let t=document.getElementById("typeImageX");this.image=t},getCookie(){let t="";if(document.cookie&&document.cookie!=="")for(var o=document.cookie.split(";"),r=0;r<o.length;r++){var a=o[r].trim();if(a.substring(0,10)==="csrftoken="){t=decodeURIComponent(a.substring(10));break}}return t}},mounted(){this.get_csrf(),this.get_users()}}),v={class:"vh-100 gradient-custom"},P={class:"container py-5 h-100"},X={class:"row d-flex justify-content-center align-items-center h-100"},E={class:"col-12 col-md-8 col-lg-6 col-xl-5"},I={class:"card bg-dark text-white",style:{"border-radius":"1rem"}},C={class:"card-body p-5 text-center"},k={class:"mb-md-5 mt-md-4 pb-5"},x=e("h2",{class:"fw-bold mb-2 text-uppercase card-text-colour"},"Signup",-1),B=e("p",{class:"mb-5 card-text-colour2"},"Please enter your login and password! ",-1),D={id:"post",class:"p-1"},S={class:"form-outline form-white mb-4"},V=e("label",{class:"form-label card-text-colour2",for:"typeEmailX"},"Email",-1),U={class:"form-outline form-white mb-4"},T=e("label",{class:"form-label card-text-colour2",for:"typePasswordX"},"Password",-1),$={class:"form-outline form-white mb-4"},A=e("label",{class:"form-label card-text-colour2",for:"typeDateX"},"Date of Birth",-1),N={class:"form-outline form-white mb-4"},j=e("label",{class:"form-label card-text-colour2",for:"typeCityX"},"City",-1),z={class:"form-outline form-white mb-4"},F=e("label",{class:"form-label card-text-colour2",for:"typeImageX"},"Upload Profile Picture",-1),G={class:"mb-0 card-text-colour2"},L=e("a",{href:"#",class:"card-text-colour2 fw-bold"},"Login",-1);function O(t,o,r,a,d,c){const m=f("router-link");return y(),g("section",v,[e("div",P,[e("div",X,[e("div",E,[e("div",I,[e("div",C,[e("div",k,[x,B,e("form",D,[e("div",S,[n(e("input",{type:"email",name:"email","onUpdate:modelValue":o[0]||(o[0]=s=>t.email=s),id:"typeEmailX",class:"form-control form-control-lg"},null,512),[[i,t.email]]),V]),e("div",U,[n(e("input",{type:"password",name:"password","onUpdate:modelValue":o[1]||(o[1]=s=>t.password=s),id:"typePasswordX",class:"form-control form-control-lg"},null,512),[[i,t.password]]),T]),e("div",$,[n(e("input",{type:"date",name:"dob",id:"typeDateX","onUpdate:modelValue":o[2]||(o[2]=s=>t.dob=s),class:"form-control form-control-lg"},null,512),[[i,t.dob]]),A]),e("div",N,[n(e("input",{type:"text",name:"city",id:"typeCityX","onUpdate:modelValue":o[3]||(o[3]=s=>t.city=s),class:"form-control form-control-lg"},null,512),[[i,t.city]]),j]),e("div",z,[e("input",{type:"file",name:"picture",id:"typeImageX",accept:"image/*",onChange:o[4]||(o[4]=s=>t.changeImage()),class:"form-control form-control-lg"},null,32),F])]),e("button",{class:"btn btn-outline-light btn-lg px-5",onClick:o[5]||(o[5]=(...s)=>t.add_user&&t.add_user(...s))},"Signup")]),e("div",null,[e("p",G,[h("Already have an account? "),_(m,{to:"/login"},{default:b(()=>[L]),_:1})])])])])])])])])}const Z=p(w,[["render",O]]);export{Z as default};