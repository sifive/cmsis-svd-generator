# cmsis-svd-generator
Generates CMSIS-SVD xml files from DTS info and Register templates in the regmaps directory.

# Generating a compatible DTS file

Many DTS files are multi-level, and have both C and DSTI includes.

To flatten the DTS file, one can run the C preprocessor and device tree compiler:

```bash
# run CPP to handle any C-style includes

cpp -nostdinc -I include -I arch  -undef -x assembler-with-cpp /path/to/input.dts > processed.dts

# run DTC to handle any DTSI includes

dtc -I dts -O dts -o output.dts processed.dts

# finally, run generate-svd.py

./generate-svd.py -o output.svd -d output.dts
```
