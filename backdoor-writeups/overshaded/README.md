overshaded
==========

Link: https://backdoor.sdslabs.co/challenges/overSHADEd \
Tags: [reversing] [n00b20ctf]

Description:
------------

You are given two files — `pixel_shader.cso` and `shader.hlsl` — and a [link to a web page](https://www.gamedev.net/forums/topic/669081-hlsl-matrix-initialization/5233874/) that hopefully provides some useful information.

Solution:
---------

The `.hlsl` extension indicates a High Level Shader Language File, which is used in 3D rendering. In this case, it just seems to define a 4×4 matrix of `float` values that have all been redacted.

```
float4x4 main() : SV_TARGET
{
    float4x4 flag = {
        REDACTED, REDACTED, REDACTED, REDACTED,
        REDACTED, REDACTED, REDACTED, REDACTED,
        REDACTED, REDACTED, REDACTED, REDACTED,
        REDACTED, REDACTED, REDACTED, REDACTED
    };

	return flag;
}
```

A `.cso` file is a Compiled Shader Object File obtained by compiling a `.hlsl` file. So presumably these redacted values are embedded in the `.cso` file somewhere. The bytes following the `SV_TARGET` label in this file look like promising candidates. There appear to be more than 16 values here, but it turns out that there *are* 16 non-zero integer values in amongst them.

I wrote a C program to extract them and print their corresponding ASCII characters in the correct order according to the linked reference:

```C
#include <stdio.h>

int main() {
    FILE *infile;
    char flag[17] = { 0 };
    int byte_order[16] = { 0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15 };
    float f;
    int i, chr;

    // Open shader file and skip past extraneous data
    infile = fopen("pixel_shader.cso", "r");
    for (i=0; i<0x110; i++) fgetc(infile);

    // Fetch float32 values and assemble the nonzero values in the correct order
    for (i=0; i<16; ) {
        // Fetch a float value and coerce to integer
        fread(&f, sizeof(float), 1, infile);
        chr = f;

        // If not zero, add to output
        if (chr) flag[byte_order[i++]] = chr;
    }
    fclose(infile);

    printf("flag{%s}\n", flag);
    return 0;
}
```
