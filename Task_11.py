from flask import Flask
app = Flask(__name__)
@app.route("/") # Route is a function which do route a user
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lilli Sharma — Dev Pro Portfolio</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap" rel="stylesheet">

<style>
:root{
    --bg:#070b12;
    --panel:#0e1621;
    --glass:rgba(255,255,255,0.14);
    --primary:#00f2ff;
    --accent:#ff2e63;
    --text:#e5e9ef;
}

*{box-sizing:border-box;scroll-behavior:smooth;}

body{
    margin:0;
    font-family:"Poppins",sans-serif;
    background:radial-gradient(circle at top,#0f1c2d,#05080e);
    color:var(--text);
    display:flex;
    overflow-x:hidden;
}

/* ================= SIDEBAR ================= */
.sidebar{
    width:220px;
    background:linear-gradient(180deg,#05080e,#0b1220);
    padding:35px 25px;
    height:100vh;
    position:fixed;
    box-shadow:8px 0 30px rgba(0,0,0,0.85);
}
.sidebar img{
    width:120px;height:120px;border-radius:50%;
    display:block;margin:auto;margin-bottom:18px;
    border:3px solid var(--primary);
    box-shadow:0 0 25px var(--primary);
}
.sidebar h2{text-align:center;margin-bottom:15px;}
.sidebar a{
    display:block;
    padding:12px;
    margin:8px 0;
    text-decoration:none;
    color:white;
    border-radius:12px;
    transition:0.35s;
    text-align:center;
}
.sidebar a:hover{
    background:rgba(0,242,255,0.15);
    transform:translateX(6px);
}

/* ================= CONTENT ================= */
.content{
    flex:1;
    margin-left:220px;
    padding:40px;
}
section{margin-bottom:100px;}
h1{color:var(--primary);}

/* ================= HERO WITH CINEMATIC TRANSITION ================= */
.hero{
    position:relative;
    overflow:hidden;
    padding:100px 40px;
    border-radius:32px;
    text-align:center;

    background:
      linear-gradient(
        120deg,
        rgba(0,242,255,0.25),
        rgba(255,46,99,0.25),
        rgba(0,242,255,0.25)
      ),
      radial-gradient(circle at top,#0f1c2d,#05080e);

    background-size:300% 300%;
    animation: bgFlow 10s ease infinite;

    box-shadow:0 40px 120px rgba(0,0,0,0.9);

    opacity:0;
    transform:scale(1.1);
}

/* background wipe */
.hero::before{
    content:"";
    position:absolute;
    inset:-40%;
    background:linear-gradient(
        45deg,
        transparent 40%,
        rgba(255,255,255,0.18) 50%,
        transparent 60%
    );
    transform:translateX(-100%);
}

/* text start state */
.hero h1,
.hero p{
    opacity:0;
    transform:translateY(40px);
    filter:blur(8px);
}

/* ACTIVE STATE */
.hero.active{
    opacity:1;
    transform:scale(1);
    transition:all 1.3s cubic-bezier(.19,1,.22,1);
}
.hero.active::before{
    animation:wipe 1.4s ease forwards;
}
.hero.active h1{
    animation:textIn 0.9s ease forwards;
    animation-delay:0.4s;
}
.hero.active p{
    animation:textIn 0.9s ease forwards;
    animation-delay:0.6s;
}

/* animations */
@keyframes wipe{
    to{transform:translateX(100%);}
}
@keyframes textIn{
    to{
        opacity:1;
        transform:none;
        filter:none;
    }
}
@keyframes bgFlow{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* ================= GLASS ================= */
.glass{
    background:linear-gradient(
        135deg,
        rgba(255,255,255,0.22),
        rgba(255,255,255,0.05)
    );
    backdrop-filter:blur(16px);
    border-radius:22px;
    padding:25px;
    border:1px solid rgba(255,255,255,0.25);
    box-shadow:0 15px 55px rgba(0,0,0,0.75);
    transition:0.4s;
}
.glass:hover{
    transform:translateY(-10px);
    box-shadow:0 25px 95px rgba(0,242,255,0.4);
}

/* ================= LAYOUT ================= */
.flex{display:flex;flex-wrap:wrap;gap:25px;}
.card{width:320px;}
.timeline{border-left:3px solid var(--primary);padding-left:30px;}
.tl-item{margin-bottom:30px;}

/* ================= FORM ================= */
form input,form textarea{
    width:100%;
    padding:12px;
    margin:10px 0;
    border-radius:14px;
    border:none;
    background:#111a27;
    color:white;
}
form button{
    padding:12px 28px;
    border:none;
    border-radius:22px;
    background:linear-gradient(135deg,var(--primary),var(--accent));
    font-weight:600;
    cursor:pointer;
}

/* ================= MOBILE ================= */
@media(max-width:850px){
    .sidebar{position:relative;width:100%;height:auto;}
    .content{margin-left:0;}
}
</style>
</head>

<body>

<div class="sidebar">
<img src="https://via.placeholder.com/150">
<h2>Lilli Sharma</h2>
<a href="#hero">Home</a>
<a href="#about">About</a>
<a href="#services">Services</a>
<a href="#projects">Projects</a>
<a href="#experience">Experience</a>
<a href="#education">Education</a>
<a href="#skills">Skills</a>
<a href="#contact">Contact</a>
</div>

<div class="content">

<section id="hero" class="hero">
<h1>Hi, I'm <span style="color:var(--accent)">Lilli Sharma</span></h1>
<p>Full-stack Developer & Designer</p>
</section>

<section id="about">
<h1>About Me</h1>
<div class="glass">
Passionate about software development, animations, UI/UX, and building interactive web applications.
</div>
</section>

<section id="services">
<h1>Services</h1>
<div class="flex">
<div class="glass card"><h2>Web Development</h2><p>Responsive websites with modern design.</p></div>
<div class="glass card"><h2>UI/UX Design</h2><p>Clean and intuitive interfaces.</p></div>
<div class="glass card"><h2>Branding</h2><p>Logo and identity design.</p></div>
</div>
</section>

<section id="projects">
<h1>Projects</h1>
<div class="flex">
<div class="glass card"><h2>Nayasa</h2><p>Circular Marketplace</p></div>
<div class="glass card"><h2>Auralis</h2><p>Full-stack App</p></div>
</div>
</section>

<section id="experience">
<h1>Experience</h1>
<div class="timeline">
<div class="glass tl-item"><h3>R&D — Indica Piezo Optics</h3><p>June–Aug, 2025</p></div>
</div>
</section>

<section id="education">
<h1>Education</h1>
<div class="timeline">
<div class="glass tl-item"><h3>BTech Computer Science</h3><p>2024–2028</p></div>
</div>
</section>

<section id="skills">
<h1>Skills</h1>
<div class="flex">
<div class="glass card">HTML</div>
<div class="glass card">CSS</div>
<div class="glass card">JavaScript</div>
<div class="glass card">React</div>
<div class="glass card">Python</div>
<div class="glass card">Django</div>
<div class="glass card">UI/UX</div>
</div>
</section>

<section id="contact">
<h1>Contact</h1>
<form class="glass">
<input type="text" placeholder="Your Name">
<input type="email" placeholder="Email">
<textarea rows="6" placeholder="Message"></textarea>
<button>Send Message</button>
</form>
</section>

</div>

<script>
window.addEventListener("load",()=>{
    document.querySelector(".hero").classList.add("active");
});
</script>

</body>
</html>

"""
@app.route("/about")
def abouta():
    return """
    <h1>jhurgiwrubhviurgwr</h1>
    """

if __name__=='__main__':
    app.run(debug = True)

