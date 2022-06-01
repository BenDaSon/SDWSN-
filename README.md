# Software-Defined Wireless Sensor Network 
 by Benson Thong, Edgar Silerio, Jeffrey Spaulding, Edgar Rodriguez, Derek Mata, Christopher Yamada

# System Diagram
![](pictures/Picture1.png)

The project utilizes a bare-metal server(VMware esxi) and OpenFlow switches(Cisco catalyst 2960-X Series) to generate the software-defined network. The server is connected to CPP's VPN which can be accessed from an IP address. A software based controller is installed on a virtual machine where an application interface called the Flow Manager developed by Maen Artimy. The project consist of 3 access points by configuring the Raspberry Pi to serve as a hotspot. Raspberry Pi that act as a sensor node are then connected to its respective access point. Because each sensor node is connected to a different access point, connectivity isn't possible among the three sensor nodes displayed in the diagram. This is where software-defined network plays a role to allow connection. Compared to traditional networks, manual configurations on each access point is done one-by-one. A software-defined network controls this using a software controller to centralize the system and control the network through a single entity. With the generation of flows in the OpenFlow  switch, an instruction is sent to the flow table of the switch to perform an action if the flow is matched with incoming packets on an ingress port of the switch. 

# Sensor Node 
![](pictures/Picture2.png)

# Ryu Controller Topology

![](pictures/topology.png)

# Generation of flows
![](pictures/flows.png)
