## Set up a GoldenGate assembly reaction using an optimised GoldenGate assembly mix

from opentrons import robot, containers, instruments

p20rack = containers.load('tiprack-10ul-H', 'B2', 'p20_rack')
tube_rack = continers.load('tube-rack-2ml', 'A1', 'tube_rack')

output = containers.load('96-PCR-flat', 'C1', 'output')
trash = containers.load('trash-box', 'C3')

p20 = instruments.Pipette(
	tip_racks=[p20rack],
	trash_containers=trash,
	min_volume = 2,
	max_volume = 20,
	axis="a"
)

water_source = tube_rack.wells('A1')
GGbuffer = tube_rack.wells('A2')
GGmix = tube_rack.wells('A3')

total_volume = 20
DNA_volumes = [2, 3, 3.5, 4, 5, 6, 6.7, 7]

water_volumes []
for v in DNA_volumes:
	water_volumes.append(total_volume - v - 4 - 2)

p20.distribute(
	water_volumes,
	water_source,
	output.wells('A1', length=DNA_volumes),
	blow_out=True,
	touch_tip=True
)

p20.distribute(
	4,
	GGbuffer,
	output.wells('A1', length=DNA_volumes),
	mix_after(4, 3),
	blow_out=True,
	touch_tip=True
)

p20.distribute(
	2,
	GGbuffer,
	output.wells('A1', length=DNA_volumes),
	mix_after(18, 5),
	blow_out=True,
	touch_tip=True
)
