
# My useless website

This is an SQLI challenge

1: connect to https://my-us3l355-w3b51t3.vishwactf.com/
2: We see that we can't enter the space characters for normal SQLI
3: When we enter credentials we see them appear in the URL, this means we can craft the URL to have the input we want
4: With Cyberchef, I crafted my input for the website: <https://gchq.github.io/CyberChef/#recipe=URL_Decode()&input=JTI3JTIwT1IlMjAlMjcxJTI3JTNEJTI3MSUyNyUyMC0tJTIw>
5: I got my flag: <https://my-us3l355-w3b51t3.vishwactf.com/?user=admin&pass=%27%20OR%20%271%27%3D%271%27%20--%20>

**Flag: VishwaCTF{I_Kn0w_Y0u_kn0W_t1hs_4lr3ady}**
