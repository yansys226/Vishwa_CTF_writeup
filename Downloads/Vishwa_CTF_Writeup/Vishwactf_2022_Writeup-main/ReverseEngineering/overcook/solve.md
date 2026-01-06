
r2 session:

```
> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze all functions arguments/locals
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Finding and parsing C++ vtables (avrr)
[x] Skipping type matching analysis in debugger mode (aaft)
[x] Propagate noreturn information (aanr)
[x] Integrate dwarf function information.
[x] Use -AA or aaaa to perform additional experimental analysis.
> afl
0x5659c080    1 49           entry0
0x5659c0b2    1 4            fcn.5659c0b2
0x5659c060    1 6            sym.imp.__libc_start_main
0x5659c0d0    4 57   -> 52   sym.deregister_tm_clones
0x5659c1b5    1 4            sym.__x86.get_pc_thunk.dx
0x5659c110    4 71           sym.register_tm_clones
0x5659c160    5 71           sym.__do_global_dtors_aux
0x5659c0c0    1 4            sym.__x86.get_pc_thunk.bx
0x5659c070    1 6            sym..plt.got
0x5659c1b0    1 5            entry.init0
0x5659c000    3 32           sym._init
0x5659c3c0    1 1            sym.__libc_csu_fini
0x5659c1e2    1 90           sym.getMessage
0x5659c040    1 6            sym.imp.gets
0x5659c030    1 6            sym.imp.printf
0x5659c3c1    1 4            sym.__x86.get_pc_thunk.bp
0x5659c3c8    1 20           sym._fini
0x5659c360    4 93           sym.__libc_csu_init
0x5659c1b9    1 41           main
0x5659c050    1 6            sym.imp.exit
0x5659c23c    1 280          sym.printflag
0x5659b000    5 110  -> 126  loc.imp._ITM_deregisterTMCloneTable
> s main
> pdf
┌ 41: int main (char **argv);
│           ; arg char **argv @ esp+0x24
│           0x5659c1b9      8d4c2404       lea ecx, [argv]
│           0x5659c1bd      83e4f0         and esp, 0xfffffff0
│           0x5659c1c0      ff71fc         push dword [ecx - 4]
│           0x5659c1c3      55             push ebp
│           0x5659c1c4      89e5           mov ebp, esp
│           0x5659c1c6      53             push ebx
│           0x5659c1c7      51             push ecx
│           0x5659c1c8      e8f3feffff     call sym.__x86.get_pc_thunk.bx
│           0x5659c1cd      81c3332e0000   add ebx, 0x2e33
│           0x5659c1d3      e80a000000     call sym.getMessage
│           0x5659c1d8      83ec0c         sub esp, 0xc
│           0x5659c1db      6a00           push 0
└           0x5659c1dd      e86efeffff     call sym.imp.exit           ; void exit(int status)
> db 0x5659c1cd
> dc
hit breakpoint at: 0x5659c1cd
> pdf
┌ 41: int main (char **argv);
│           ; arg char **argv @ esp+0x24
│           0x5659c1b9      8d4c2404       lea ecx, [argv]
│           0x5659c1bd      83e4f0         and esp, 0xfffffff0
│           0x5659c1c0      ff71fc         push dword [ecx - 4]
│           0x5659c1c3      55             push ebp
│           0x5659c1c4      89e5           mov ebp, esp
│           0x5659c1c6      53             push ebx
│           0x5659c1c7      51             push ecx
│           0x5659c1c8      e8f3feffff     call sym.__x86.get_pc_thunk.bx
│           ;-- ebx:
│           ;-- eip:
│           0x5659c1cd b    81c3332e0000   add ebx, 0x2e33
│           0x5659c1d3      e80a000000     call sym.getMessage
│           0x5659c1d8      83ec0c         sub esp, 0xc
│           0x5659c1db      6a00           push 0
└           0x5659c1dd      e86efeffff     call sym.imp.exit           ; void exit(int status)
> dr
eax = 0xf7f32ae8
ebx = 0x5659c1cd
ecx = 0xff8f1040
edx = 0xff8f1074
esi = 0xf7f30000
edi = 0xf7f30000
esp = 0xff8f1020
ebp = 0xff8f1028
eip = 0x5659c1cd
eflags = 0x00000286
oeax = 0xffffffff
> dr eip = 0x5659c23c
0x5659c1cd ->0x5659c23c
> dc

114
051
118
101
114
115
049
110
103
095
100
117
100
051
```

The numbers being decimal we can reverse them quickly: <https://gchq.github.io/CyberChef/#recipe=From_Decimal('Line%20feed',false)&input=MTE0CjA1MQoxMTgKMTAxCjExNAoxMTUKMDQ5CjExMAoxMDMKMDk1CjEwMAoxMTcKMTAwCjA1MQ>

**VishwaCTF{r3vers1ng_dud3}**
