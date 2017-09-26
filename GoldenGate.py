## Set up a GoldenGate assembly reaction using an optimised GoldenGate assembly mix

from opentrons import robot, containers, instruments

#Create 6x12 p20 tip rack container
containers.create(
'6x12-tiprack',
grid=(6,12),
spacing=(9, 9),
diameter=5,
depth=60
)

#Create 3x6 2ml tube rack for DNA samples
containers.create(
'3x6-tube-rack-2ml',
grid=(3,6),
spacing=(19.5,19.5),
diameter=9.5,
depth=40
)

#Specify containers
p20rack = containers.load('6x12-tiprack', 'B2', 'p20_rack')
tube_rack = containers.load('tube-rack-2ml', 'D1', 'tube_rack')
cool_rack = containers.load('tube-rack-2ml', 'E3', 'cool_rack')
DNA_rack = containers.load('3x6-tube-rack-2ml', 'C3', 'DNA_rack')

output = containers.load('96-PCR-flat', 'C1', 'output')
trash = containers.load('trash-box', 'A3')

p20 = instruments.Pipette(
	tip_racks=[p20rack],
	trash_container=trash,
	min_volume = 2,
	max_volume = 20,
	axis="a"
)

water_source = tube_rack.wells('A1')
GGbuffer = tube_rack.wells('A2')
GGmix = cool_rack.wells('A1')

total_volume = 20
DNA_volumes = [2, 3, 3.5, 4, 5, 6, 7, 8]
num_assemblies = len(DNA_volumes)

water_volumes = []
for v in DNA_volumes:
	water_volumes.append(total_volume - v - 4 - 2)

p20.transfer(
    water_volumes,
    water_source,
    output.wells('A1', length=num_assemblies),
    blow_out=True,
    touch_tip=True
)

p20.transfer(
	4,
	GGbuffer,
	output.wells('A1', length=num_assemblies),
	mix_after = (3, 4),
	blow_out=True,
	touch_tip=True,
	new_tip='always'
)

p20.transfer(
	DNA_volumes,
	DNA_rack.wells('A1', length=num_assemblies),
	output.wells('A1', length=num_assemblies),
	mix_after = (3, 8),
	blow_out=True,
	touch_tip=True,
	new_tip='always'
)

p20.transfer(
	2,
	GGmix,
	output.wells('A1', length=num_assemblies),
	mix_after = (5, 18),
	blow_out=True,
	touch_tip=True,
	new_tip='always'
)
