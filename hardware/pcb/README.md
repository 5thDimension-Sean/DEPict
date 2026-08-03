# PCB

KiCad 8+ project for the DEPict carrier board. (Design files to be added.)

Expected files once designed:

- `depict.kicad_pro` — project
- `depict.kicad_sch` — schematic
- `depict.kicad_pcb` — layout
- `gerbers/` — fabrication outputs
- `depict.kicad_pcb → ../schematics/depict.pdf` — exported for review

Run ERC + DRC before exporting gerbers. Export the BOM to `../bom/bom.csv`.
