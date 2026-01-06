# **My Useless Website**

We need to connect to this site: <https://my-us3l355-w3b51t3.vishwactf.com/>.

We want to try a quick SQLI payload like "' OR 1=1 -- ", to see if this is the vulnerability they want us to exploit. But we realise that the space input has been disabled.

We solve this using 2 ways.

1. Copying our payload and pasting it in the fields.
2. When entering data in the fields, they end up in the url: <https://my-us3l355-w3b51t3.vishwactf.com/?user=a&pass=b> (attempt with username a and password b). A quick URL encode of our payload and we can just inject it in the url: <https://gchq.github.io/CyberChef/#recipe=URL_Encode(false)&input=JyBPUiAxPTEgLS0g>, final url: <https://my-us3l355-w3b51t3.vishwactf.com/?user=%27%20OR%201=1%20--%20&pass=%27%20OR%201=1%20--%20>.

The flag is given after that: **VishwaCTF{I_Kn0w_Y0u_kn0W_t1hs_4lr3ady}**.

---


