/* ===========================
   rksoftwareservices PREMIUM JS
=========================== */

/* Reveal Animation */

const reveals =
document.querySelectorAll(".reveal");

window.addEventListener("scroll", () => {

    reveals.forEach((el) => {

        let top =
            el.getBoundingClientRect().top;

        let height =
            window.innerHeight - 100;

        if(top < height){

            el.classList.add("active");
        }
    });
});

/* ===========================
   Counter Animation
=========================== */

const counters =
document.querySelectorAll(".counter");

const startCounter = () => {

    counters.forEach(counter => {

        const target =
            +counter.dataset.target;

        let count = 0;

        const speed = target / 150;

        const update = () => {

            count += speed;

            if(count < target){

                counter.innerText =
                    Math.floor(count);

                requestAnimationFrame(update);

            }else{

                counter.innerText =
                    target;
            }
        }

        update();
    });
}

const counterSection =
document.querySelector(".counter-section");

if(counterSection){

    const observer =
    new IntersectionObserver(entries=>{

        if(entries[0].isIntersecting){

            startCounter();
        }

    });

    observer.observe(counterSection);
}

/* ===========================
   Navbar Scroll Effect
=========================== */

window.addEventListener("scroll",()=>{

    const navbar =
    document.querySelector(".navbar");

    if(window.scrollY > 50){

        navbar.style.background =
        "rgba(5,8,22,.95)";

    }else{

        navbar.style.background =
        "rgba(5,8,22,.65)";
    }
});

/* ===========================
   Smooth Scroll
=========================== */

document.querySelectorAll('a[href^="#"]')
.forEach(anchor=>{

    anchor.addEventListener("click",function(e){

        e.preventDefault();

        document.querySelector(
            this.getAttribute("href")
        ).scrollIntoView({

            behavior:"smooth"
        });
    });
});

/* ===========================
   Mouse Glow Effect
=========================== */

const glow =
document.createElement("div");

glow.style.position="fixed";
glow.style.width="300px";
glow.style.height="300px";
glow.style.borderRadius="50%";
glow.style.pointerEvents="none";
glow.style.background=
"radial-gradient(circle, rgba(37,99,235,.25), transparent 70%)";
glow.style.zIndex="-1";

document.body.appendChild(glow);

document.addEventListener("mousemove",(e)=>{

    glow.style.left =
    (e.clientX - 150) + "px";

    glow.style.top =
    (e.clientY - 150) + "px";
});

/* ===========================
   Typing Effect
=========================== */

const text =
"Software Development & Technology Solutions";

const typing =
document.getElementById("typing");

if(typing){

    let i = 0;

    function type(){

        if(i < text.length){

            typing.innerHTML += text.charAt(i);

            i++;

            setTimeout(type,60);
        }
    }

    type();
}

/* ===========================
   Back To Top
=========================== */

const topBtn =
document.getElementById("topBtn");

if(topBtn){

window.addEventListener("scroll",()=>{

    if(window.scrollY > 400){

        topBtn.style.display="block";

    }else{

        topBtn.style.display="none";
    }

});

topBtn.addEventListener("click",()=>{

    window.scrollTo({

        top:0,
        behavior:"smooth"
    });

});
}