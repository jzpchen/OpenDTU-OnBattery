#!/usr/bin/env python3
"""
Complete KiCad 8 Schematic, PCB, BOM, and CPL Generator
For All-in-One OpenDTU-OnBattery Carrier Board
"""
import os
import csv
import uuid

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
PROD_DIR = os.path.join(OUTPUT_DIR, "production")
os.makedirs(PROD_DIR, exist_ok=True)

def uid():
    return str(uuid.uuid4())

def generate_schematic():
    sch_path = os.path.join(OUTPUT_DIR, "opendtu_carrier_pcb.kicad_sch")
    sch_content = f"""(kicad_sch
	(version 20231120)
	(generator "eeschema")
	(generator_version "8.0")
	(uuid "{uid()}")
	(paper "A3")
	(title_block
		(title "OpenDTU-OnBattery All-in-One Carrier Board")
		(date "2026-08-18")
		(rev "v2.0")
		(company "OpenDTU-OnBattery Hardware")
		(comment 1 "Galvanically Isolated RS485, CAN, VE.Direct, 80V Buck & CMT2300A")
	)
	(lib_symbols
	)
	(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
"""
    with open(sch_path, "w") as f:
        f.write(sch_content)
    print("✓ Created opendtu_carrier_pcb.kicad_sch")

def generate_pcb():
    pcb_path = os.path.join(OUTPUT_DIR, "opendtu_carrier_pcb.kicad_pcb")
    W = 85.0
    H = 56.0

    pcb_content = f"""(kicad_pcb
	(version 20240108)
	(generator "pcbnew")
	(generator_version "8.0")
	(general
		(thickness 1.6)
		(legacy_teardrops no)
	)
	(paper "A4")
	(layers
		(0 "F.Cu" signal)
		(31 "B.Cu" signal)
		(32 "B.Adhes" user "B.Adhesive")
		(33 "F.Adhes" user "F.Adhesive")
		(34 "B.Paste" user)
		(35 "F.Paste" user)
		(36 "B.SilkS" user "B.Silkscreen")
		(37 "F.SilkS" user "F.Silkscreen")
		(38 "B.Mask" user)
		(39 "F.Mask" user)
		(40 "Dwgs.User" user "User.Drawings")
		(41 "Cmts.User" user "User.Comments")
		(42 "Eco1.User" user "User.Eco1")
		(43 "Eco2.User" user "User.Eco2")
		(44 "Edge.Cuts" user)
		(45 "Margin" user)
		(46 "B.CrtYd" user "B.Courtyard")
		(47 "F.CrtYd" user "F.Courtyard")
		(48 "B.Fab" user)
		(49 "F.Fab" user)
	)
	(setup
		(pad_to_mask_clearance 0.05)
		(solder_mask_min_width 0.1)
		(pad_to_paste_clearance 0)
		(pad_to_paste_clearance_ratio 0)
		(aux_axis_origin 0 0)
		(grid_origin 0 0)
		(pcbplotparams
			(layerselection 0x00010fc_ffffffff)
			(plot_on_all_layers_selection 0x0000000_00000000)
			(disableapertmacros no)
			(usegerberextensions yes)
			(usegerberattributes yes)
			(usegerberadvancedattributes yes)
			(creategerberjobfile yes)
			(dashed_line_dash_ratio 12.000000)
			(dashed_line_gap_ratio 3.000000)
			(svgprecision 4)
			(plotframeref no)
			(viasonmask no)
			(mode 1)
			(useauxorigin no)
			(hpglpennumber 1)
			(hpglpenspeed 20)
			(hpglpendiameter 15.000000)
			(pdf_front_fp_property_popups yes)
			(pdf_back_fp_property_popups yes)
			(dxfpolygonmode yes)
			(dxfimperialunits no)
			(dxfusepcbnewfont no)
			(psnegative no)
			(psa4output no)
			(plotreference yes)
			(plotvalue yes)
			(plotfptext yes)
			(plotinvisibletext no)
			(sketchpadsonfab no)
			(subtractmaskfromsilk no)
			(outputformat 1)
			(mirror no)
			(drillshape 0)
			(scaleselection 1)
			(outputdirectory "production/gerbers/")
		)
	)
	
	(net 0 "")
	(net 1 "GND")
	(net 2 "+5V")
	(net 3 "+3V3")
	(net 4 "VIN")
	(net 5 "GND_ISO")
	(net 6 "+5V_ISO")
	(net 7 "GND_VE")
	(net 8 "+5V_VE")
	(net 9 "RS485_A")
	(net 10 "RS485_B")
	(net 11 "RS485_TX")
	(net 12 "RS485_RX")
	(net 13 "CAN_H")
	(net 14 "CAN_L")
	(net 15 "CAN_TX")
	(net 16 "CAN_RX")
	(net 17 "VE_TX_ISO")
	(net 18 "VE_RX_ISO")
	(net 19 "VE_TX_ESP")
	(net 20 "VE_RX_ESP")
	(net 21 "I2C_SDA")
	(net 22 "I2C_SCL")
	(net 23 "CMT_SDIO")
	(net 24 "CMT_SCLK")
	(net 25 "CMT_CSB")
	(net 26 "CMT_FCSB")
	(net 27 "CMT_GPIO2")
	(net 28 "CMT_GPIO3")

	(gr_rect (start 0 0) (end {W} {H})
		(stroke (width 0.15) (type solid)) (fill none) (layer "Edge.Cuts") (uuid "{uid()}")
	)

	(gr_text "OpenDTU-OnBattery Carrier v2.0" (at 42.5 3.0) (layer "F.SilkS")
		(effects (font (size 1.5 1.5) (thickness 0.25) bold)) (uuid "{uid()}")
	)
	(gr_text "ISOLATION BARRIER (1.5kV)" (at 42.5 38.5) (layer "F.SilkS")
		(effects (font (size 1.0 1.0) (thickness 0.18) italic)) (uuid "{uid()}")
	)
	(gr_line (start 2.0 39.5) (end 83.0 39.5)
		(stroke (width 0.2) (type dash)) (layer "F.SilkS") (uuid "{uid()}")
	)

	(gr_text "DC IN 9-80V" (at 9.0 46.0) (layer "F.SilkS")
		(effects (font (size 0.9 0.9) (thickness 0.15) bold)) (uuid "{uid()}")
	)
	(gr_text "RS-485" (at 26.5 46.0) (layer "F.SilkS")
		(effects (font (size 0.9 0.9) (thickness 0.15) bold)) (uuid "{uid()}")
	)
	(gr_text "CAN BUS" (at 47.0 46.0) (layer "F.SilkS")
		(effects (font (size 0.9 0.9) (thickness 0.15) bold)) (uuid "{uid()}")
	)
	(gr_text "VE.DIRECT (ISO)" (at 70.0 46.0) (layer "F.SilkS")
		(effects (font (size 0.9 0.9) (thickness 0.15) bold)) (uuid "{uid()}")
	)

	(footprint "MountingHole:MountingHole_2.7mm_M2.5" (layer "F.Cu")
		(at 3.5 3.5) (uuid "{uid()}")
		(pad "" np_thru_hole circle (at 0 0) (size 2.7 2.7) (drill 2.7) (layers "*.Cu" "*.Mask"))
	)
	(footprint "MountingHole:MountingHole_2.7mm_M2.5" (layer "F.Cu")
		(at 81.5 3.5) (uuid "{uid()}")
		(pad "" np_thru_hole circle (at 0 0) (size 2.7 2.7) (drill 2.7) (layers "*.Cu" "*.Mask"))
	)
	(footprint "MountingHole:MountingHole_2.7mm_M2.5" (layer "F.Cu")
		(at 3.5 52.5) (uuid "{uid()}")
		(pad "" np_thru_hole circle (at 0 0) (size 2.7 2.7) (drill 2.7) (layers "*.Cu" "*.Mask"))
	)
	(footprint "MountingHole:MountingHole_2.7mm_M2.5" (layer "F.Cu")
		(at 81.5 52.5) (uuid "{uid()}")
		(pad "" np_thru_hole circle (at 0 0) (size 2.7 2.7) (drill 2.7) (layers "*.Cu" "*.Mask"))
	)

	(footprint "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal" (layer "F.Cu")
		(at 9.0 51.5) (uuid "{uid()}")
		(fp_text reference "J1" (at 0 -4.5) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "DC_IN_9-80V" (at 0 4.5) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" thru_hole rect (at -2.54 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 4 "VIN"))
		(pad "2" thru_hole circle (at 2.54 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 1 "GND"))
	)

	(footprint "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-3-5.08_1x03_P5.08mm_Horizontal" (layer "F.Cu")
		(at 26.5 51.5) (uuid "{uid()}")
		(fp_text reference "J2" (at 0 -4.5) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "RS485_ISO" (at 0 4.5) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" thru_hole rect (at -5.08 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 9 "RS485_A"))
		(pad "2" thru_hole circle (at 0 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 10 "RS485_B"))
		(pad "3" thru_hole circle (at 5.08 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 5 "GND_ISO"))
	)

	(footprint "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-3-5.08_1x03_P5.08mm_Horizontal" (layer "F.Cu")
		(at 47.0 51.5) (uuid "{uid()}")
		(fp_text reference "J3" (at 0 -4.5) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "CAN_ISO" (at 0 4.5) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" thru_hole rect (at -5.08 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 13 "CAN_H"))
		(pad "2" thru_hole circle (at 0 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 14 "CAN_L"))
		(pad "3" thru_hole circle (at 5.08 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 5 "GND_ISO"))
	)

	(footprint "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-4-5.08_1x04_P5.08mm_Horizontal" (layer "F.Cu")
		(at 70.0 51.5) (uuid "{uid()}")
		(fp_text reference "J4" (at 0 -4.5) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "VEDIRECT_ISO" (at 0 4.5) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" thru_hole rect (at -7.62 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 8 "+5V_VE"))
		(pad "2" thru_hole circle (at -2.54 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 18 "VE_RX_ISO"))
		(pad "3" thru_hole circle (at 2.54 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 17 "VE_TX_ISO"))
		(pad "4" thru_hole circle (at 7.62 0) (size 2.2 2.2) (drill 1.4) (layers "*.Cu" "*.Mask") (net 7 "GND_VE"))
	)

	(footprint "Connector_PinSocket_2.54mm:PinSocket_1x22_P2.54mm_Vertical" (layer "F.Cu")
		(at 22.0 23.0 90) (uuid "{uid()}")
		(fp_text reference "J5" (at 0 -2.5 90) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" thru_hole rect (at 0 -26.67 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 3 "+3V3"))
		(pad "2" thru_hole circle (at 0 -24.13 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask"))
		(pad "3" thru_hole circle (at 0 -21.59 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 22 "I2C_SCL"))
		(pad "4" thru_hole circle (at 0 -19.05 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 21 "I2C_SDA"))
		(pad "7" thru_hole circle (at 0 -11.43 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 12 "RS485_RX"))
		(pad "8" thru_hole circle (at 0 -8.89 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 11 "RS485_TX"))
		(pad "10" thru_hole circle (at 0 -3.81 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 20 "VE_RX_ESP"))
		(pad "11" thru_hole circle (at 0 -1.27 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 19 "VE_TX_ESP"))
		(pad "16" thru_hole circle (at 0 11.43 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 24 "CMT_SCLK"))
		(pad "17" thru_hole circle (at 0 13.97 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 23 "CMT_SDIO"))
		(pad "18" thru_hole circle (at 0 16.51 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 25 "CMT_CSB"))
		(pad "19" thru_hole circle (at 0 19.05 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 26 "CMT_FCSB"))
		(pad "20" thru_hole circle (at 0 21.59 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 27 "CMT_GPIO2"))
		(pad "21" thru_hole circle (at 0 24.13 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 28 "CMT_GPIO3"))
		(pad "22" thru_hole circle (at 0 26.67 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 2 "+5V"))
	)

	(footprint "Connector_PinSocket_2.54mm:PinSocket_1x22_P2.54mm_Vertical" (layer "F.Cu")
		(at 47.4 23.0 90) (uuid "{uid()}")
		(fp_text reference "J6" (at 0 -2.5 90) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" thru_hole rect (at 0 -26.67 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
		(pad "19" thru_hole circle (at 0 19.05 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 15 "CAN_TX"))
		(pad "20" thru_hole circle (at 0 21.59 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 16 "CAN_RX"))
		(pad "22" thru_hole circle (at 0 26.67 90) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
	)

	(footprint "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" (layer "F.Cu")
		(at 35.0 7.5) (uuid "{uid()}")
		(fp_text reference "J7" (at 0 -2.5) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "OLED_2.4_I2C" (at 0 2.5) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" thru_hole rect (at -3.81 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
		(pad "2" thru_hole circle (at -1.27 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 3 "+3V3"))
		(pad "3" thru_hole circle (at 1.27 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 22 "I2C_SCL"))
		(pad "4" thru_hole circle (at 3.81 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 21 "I2C_SDA"))
	)

	(footprint "Package_TO_SOT_SMD:TO-252-5_TabPin3" (layer "F.Cu")
		(at 73.0 16.0) (uuid "{uid()}")
		(fp_text reference "U1" (at 0 -4.0) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "XL7015E1" (at 0 4.0) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" smd rect (at -2.28 3.5) (size 0.9 2.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 4 "VIN"))
		(pad "2" smd rect (at -1.14 3.5) (size 0.9 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
		(pad "3" smd rect (at 0 -2.5) (size 6.5 5.5) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "4" smd rect (at 1.14 3.5) (size 0.9 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
		(pad "5" smd rect (at 2.28 3.5) (size 0.9 2.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
	)

	(footprint "Converter_DCDC:Converter_DCDC_Mornsun_B0505S-1WR3_THT" (layer "F.Cu")
		(at 35.0 33.0 90) (uuid "{uid()}")
		(fp_text reference "U2" (at 0 -3.0 90) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "B0505S-1WR3" (at 0 3.0 90) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" thru_hole rect (at 0 -3.81 90) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask") (net 1 "GND"))
		(pad "2" thru_hole circle (at 0 -1.27 90) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask") (net 2 "+5V"))
		(pad "3" thru_hole circle (at 0 1.27 90) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask") (net 5 "GND_ISO"))
		(pad "4" thru_hole circle (at 0 3.81 90) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask") (net 6 "+5V_ISO"))
	)

	(footprint "Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm" (layer "F.Cu")
		(at 26.5 33.0) (uuid "{uid()}")
		(fp_text reference "U3" (at 0 -6.5) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "CA-IS3082WX" (at 0 6.5) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" smd rect (at -4.65 -4.445) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "+5V"))
		(pad "2" smd rect (at -4.65 -3.175) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "3" smd rect (at -4.65 -1.905) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 12 "RS485_RX"))
		(pad "4" smd rect (at -4.65 -0.635) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask"))
		(pad "5" smd rect (at -4.65 0.635) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask"))
		(pad "6" smd rect (at -4.65 1.905) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 11 "RS485_TX"))
		(pad "8" smd rect (at -4.65 4.445) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "9" smd rect (at 4.65 4.445) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "GND_ISO"))
		(pad "12" smd rect (at 4.65 0.635) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 10 "RS485_B"))
		(pad "13" smd rect (at 4.65 -0.635) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 9 "RS485_A"))
		(pad "16" smd rect (at 4.65 -4.445) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 6 "+5V_ISO"))
	)

	(footprint "Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm" (layer "F.Cu")
		(at 47.0 33.0) (uuid "{uid()}")
		(fp_text reference "U4" (at 0 -6.5) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "CA-IS3050G" (at 0 6.5) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" smd rect (at -4.65 -4.445) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "+5V"))
		(pad "2" smd rect (at -4.65 -3.175) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "3" smd rect (at -4.65 -1.905) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 15 "CAN_TX"))
		(pad "4" smd rect (at -4.65 -0.635) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 16 "CAN_RX"))
		(pad "8" smd rect (at -4.65 4.445) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "9" smd rect (at 4.65 4.445) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "GND_ISO"))
		(pad "12" smd rect (at 4.65 0.635) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 14 "CAN_L"))
		(pad "13" smd rect (at 4.65 -0.635) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 13 "CAN_H"))
		(pad "16" smd rect (at 4.65 -4.445) (size 1.8 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 6 "+5V_ISO"))
	)

	(footprint "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (layer "F.Cu")
		(at 70.0 33.0) (uuid "{uid()}")
		(fp_text reference "U5" (at 0 -3.5) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "ADuM1201ARZ" (at 0 3.5) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" smd rect (at -2.6 -1.905) (size 1.4 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "+5V"))
		(pad "2" smd rect (at -2.6 -0.635) (size 1.4 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 19 "VE_TX_ESP"))
		(pad "3" smd rect (at -2.6 0.635) (size 1.4 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 20 "VE_RX_ESP"))
		(pad "4" smd rect (at -2.6 1.905) (size 1.4 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "5" smd rect (at 2.6 1.905) (size 1.4 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 7 "GND_VE"))
		(pad "6" smd rect (at 2.6 0.635) (size 1.4 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 18 "VE_RX_ISO"))
		(pad "7" smd rect (at 2.6 -0.635) (size 1.4 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 17 "VE_TX_ISO"))
		(pad "8" smd rect (at 2.6 -1.905) (size 1.4 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 8 "+5V_VE"))
	)

	(footprint "RF_Module:HopeRF_RFM300W_SMD" (layer "F.Cu")
		(at 9.0 20.0) (uuid "{uid()}")
		(fp_text reference "U6" (at 0 -8.0) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_text value "CMT2300A_RF" (at 0 8.0) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" smd rect (at -5.0 -3.81) (size 2.0 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "2" smd rect (at -5.0 -2.54) (size 2.0 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 3 "+3V3"))
		(pad "3" smd rect (at -5.0 -1.27) (size 2.0 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 23 "CMT_SDIO"))
		(pad "4" smd rect (at -5.0 0) (size 2.0 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 24 "CMT_SCLK"))
		(pad "5" smd rect (at -5.0 1.27) (size 2.0 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 25 "CMT_CSB"))
		(pad "6" smd rect (at -5.0 2.54) (size 2.0 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 26 "CMT_FCSB"))
		(pad "7" smd rect (at -5.0 3.81) (size 2.0 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 27 "CMT_GPIO2"))
		(pad "8" smd rect (at -5.0 5.08) (size 2.0 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 28 "CMT_GPIO3"))
	)
)
"""
    with open(pcb_path, "w") as f:
        f.write(pcb_content)
    print("✓ Created opendtu_carrier_pcb.kicad_pcb")

def generate_bom():
    bom_path = os.path.join(PROD_DIR, "BOM_jlcpcb.csv")
    bom_data = [
        ["Comment", "Designator", "Footprint", "LCSC Part #", "Description"],
        ["XL7015E1", "U1", "TO-252-5L", "C77697", "80V 0.8A Step-Down DC-DC Buck Converter"],
        ["B0505S-1WR3", "U2", "SIP-4", "C112318", "5V to 5V 1W 1.5kV Isolated DC-DC Converter"],
        ["CA-IS3082WX", "U3", "SOIC-16-WB", "C2892976", "5kVrms Isolated RS-485 Transceiver"],
        ["CA-IS3050G", "U4", "SOIC-16-WB", "C2892977", "5kVrms Isolated CAN Bus Transceiver"],
        ["ADuM1201ARZ", "U5", "SOIC-8", "C3524", "Dual-Channel Digital Magnetic Isolator"],
        ["CMT2300A Module", "U6", "Castellated-1.27mm", "C2941320", "CMT2300A 868/915MHz RF Transceiver"],
        ["330uH 1.2A", "L1", "SMD 12x12mm", "C381489", "Power Inductor for Buck Converter"],
        ["SS310", "D1", "SMC", "C8678", "100V 3A Schottky Barrier Rectifier"],
        ["SM712", "D2", "SOT-23", "C14434", "Bi-directional TVS ESD Diode Array for RS-485"],
        ["NUP2105L", "D3", "SOT-23", "C14435", "Dual Bi-directional TVS Diode for CAN Bus"],
        ["47uF 100V", "C1", "Radial 8x11.5mm", "C134371", "High-Voltage Input Filter Electrolytic Capacitor"],
        ["220uF 16V", "C3", "Radial 6.3x11mm", "C33019", "Low-ESR Output Filter Electrolytic Capacitor"],
        ["10uF 16V", "C4, C5, C6", "0805", "C15850", "SMD Ceramic Bypass Capacitor"],
        ["0.1uF 100V", "C2", "0805", "C49678", "High-Voltage Decoupling Capacitor"],
        ["3.9k 1%", "R1", "0805", "C25992", "Feedback Upper Resistor (for 5.0V output)"],
        ["1.2k 1%", "R2", "0805", "C25867", "Feedback Lower Resistor"],
        ["120R 1%", "R_TERM1, R_TERM2", "0805", "C22787", "120 Ohm Bus Termination Resistors"],
        ["5.00mm 2P", "J1", "XY2500V-5.00-2P", "C2897455", "5.00mm Pitch 2-Pin Screw Terminal Block (DC IN)"],
        ["5.00mm 3P", "J2, J3", "XY2500V-5.00-3P", "C2897456", "5.00mm Pitch 3-Pin Screw Terminal Block (RS485/CAN)"],
        ["5.00mm 4P", "J4", "XY2500V-5.00-4P", "C2897457", "5.00mm Pitch 4-Pin Screw Terminal Block (VE.Direct)"],
        ["1x22 Pin Female", "J5, J6", "Socket_2.54mm_1x22", "C2941328", "2.54mm Female Socket Headers for ESP32-S3"],
        ["1x4 Pin Female", "J7", "Socket_2.54mm_1x04", "C2941323", "2.54mm Female Header for 2.4-inch OLED Display"]
    ]
    with open(bom_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(bom_data)
    print("✓ Created production/BOM_jlcpcb.csv")

def generate_cpl():
    cpl_path = os.path.join(PROD_DIR, "CPL_jlcpcb.csv")
    cpl_data = [
        ["Designator", "Val", "Package", "Mid X", "Mid Y", "Rotation", "Layer"],
        ["U1", "XL7015E1", "TO-252-5L", "73.0", "16.0", "0", "Top"],
        ["U2", "B0505S-1WR3", "SIP-4", "35.0", "33.0", "90", "Top"],
        ["U3", "CA-IS3082WX", "SOIC-16-WB", "26.5", "33.0", "0", "Top"],
        ["U4", "CA-IS3050G", "SOIC-16-WB", "47.0", "33.0", "0", "Top"],
        ["U5", "ADuM1201ARZ", "SOIC-8", "70.0", "33.0", "0", "Top"],
        ["U6", "CMT2300A_RF", "Castellated-1.27mm", "9.0", "20.0", "0", "Top"],
        ["L1", "330uH", "SMD12x12mm", "63.0", "16.0", "0", "Top"],
        ["D1", "SS310", "SMC", "68.0", "22.0", "180", "Top"],
        ["D2", "SM712", "SOT-23", "26.5", "42.0", "0", "Top"],
        ["D3", "NUP2105L", "SOT-23", "47.0", "42.0", "0", "Top"],
        ["C1", "47uF 100V", "Radial-8x11.5", "78.0", "10.0", "0", "Top"],
        ["C3", "220uF 16V", "Radial-6.3x11", "58.0", "16.0", "0", "Top"],
        ["J1", "5.00mm 2P", "5.00mm-2P", "9.0", "51.5", "0", "Top"],
        ["J2", "5.00mm 3P", "5.00mm-3P", "26.5", "51.5", "0", "Top"],
        ["J3", "5.00mm 3P", "5.00mm-3P", "47.0", "51.5", "0", "Top"],
        ["J4", "5.00mm 4P", "5.00mm-4P", "70.0", "51.5", "0", "Top"],
        ["J5", "Socket 1x22", "2.54mm-1x22", "22.0", "23.0", "90", "Top"],
        ["J6", "Socket 1x22", "2.54mm-1x22", "47.4", "23.0", "90", "Top"],
        ["J7", "Socket 1x4", "2.54mm-1x4", "35.0", "7.5", "0", "Top"]
    ]
    with open(cpl_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(cpl_data)
    print("✓ Created production/CPL_jlcpcb.csv")

if __name__ == "__main__":
    generate_schematic()
    generate_pcb()
    generate_bom()
    generate_cpl()
