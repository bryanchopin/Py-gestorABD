ll = ['Math.abs, Math.exp,Math.log,Math.log10,Math.log1p,Math.log2,Math.max, Math.min,Math.random, Math.sor, Math.shuffle,Math.choice,Math.round,Math.sqrt, Math.pow,Math.ceil,Math.floor,Math.cbrt,Math.exp,Math.sign,Math.randint, Math.random.normal, Math.random.binomial,Math.random.poiss on,Math.random.uniform,Math.random.logi stic, Math.random.multinomial,Math.random.exponential,Math.random.chisquare,Math.random.rayleigh,Math.random.paret o,Math.lcm, Math.gcd,Math.trunc,Math.fix, Math.around,Math.hypot,Math.deg2rad, Math.rad2de, Math.quadratic, Math.cubic,Math.squareArea, Math.rectArea,Math.circleArea, Math.triangleArea,Math.trapArea, Math.regpolyArea,Math.bigmul,Math.BitDe crement, Math.BitIncrement,Math.Clamp,Math.Copy Sing,Math.DivRem,Math.FusedMultiplyAdd,Math.MaxMagnitude,Math.MinMagnitude,Math.pi,Math.scale,Math.scaleB,Math.sign']
# campoo = str(campo).replace(","," | ")
lll = ['Math.acos,Math.acosh,Math.asin,Math.asi nh,Math.atan,Math.atan2,Math.atanh,Math.cos,Math.cosh,Math.sin,Math.sinh,Mat.t an,Math.tanh']

lq = ['Capitalize,casefold,center,count,encode,endswith,Expandtabs,find,format,format_map,index,isalnum,Isalpha,isascii,isdecimal,isdigit,islower,isnumeric,Isprintable,isspace,istitle,issupper,join,lower,istrip,Maketrans,partition,replace,rindex,rjust,rsplit,rstrip,Split,upper,zfill']

l = ['int,char,float,short,long,byte,double,sbyte, string,uint,ulong,integer,Boolean,const,enu m,dynamic,tuple']

A = ['<html>,</html>,<head>,</head>,<header>,</header>,<body>,</body>,<meta>,<div>,</div>,<section>,</section>,<article>,</article>,<image>,</image>,<script>,</script>,<p>,</p>,<h1>,</h1>,<h2>,</h2>,<h3>,</h3>,<title>,</title>,<style>,</style>,<nav>,</nav>,<main>,</main>,<footer>,</fooer>,<li>,</li>,<ul>,</ul>,<a>,</a>,<table>,<dt>,<th>,<figure>,<map>,<span>,<br>']
llll = ['Console.readkey,Console.readline,Consol e.writeline,Console.write,print,println,scan,scanf,input'] 
A = str(A).replace(",",'|')
print(A)




link = False
atributo = input("").split(",")

tipos = ["caracter","entero","decimal","fecha"]

for x in tipos:
    if atributo[1] == x:
        link = True

if len(atributo) == 3 and link:
    print("success")
else:
    print("error")


lista = ["3.4","hola","2"]


a = "hola"
w = 3
print(type(a))
print(type(w))

print(float(l))

