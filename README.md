# poppy-buggy

Poppy Buggy is a **Poppy creature** combining a [Poppy Ergo Jr](https://github.com/poppy-project/poppy-ergo-jr) robotic arm, a two-wheeled chassis and batteries for autonomous operation.

Poppy creatures are built from [XL320 motors](http://support.robotis.com/en/product/dynamixel/xl-series/xl-320.htm) from [Robotis](http://en.robotis.com/index/). Motors are linked together with [parametrable frames](https://github.com/jgrizou/robotis-scad) designed with [OpenScad](http://www.openscad.org/). The resulting robots are controlled using the [pypot library](https://github.com/poppy-project/pypot), typically running on a Raspberry Pi. These robots aim at being low cost and easy to modify.

The repository includes a hardware, a software, and a doc folder:
- The [hardware](hardware) folder contains the 3D parts..
- The [software](software) folder contains the [pypot](https://github.com/poppy-project/pypot) config files specific to your robot.
- The [doc](doc) folder contains the documentation.

