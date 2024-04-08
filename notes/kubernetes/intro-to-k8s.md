## Table of Contents

#### Monolith vs Microservices
A monolith has a rather expensive taste in hardware. Being a large, single piece of software which continuously grows, it has to run on a single system which has to satisfy its compute, memory, storage, and networking requirements. The hardware of such capacity is not only complex and extremely pricey, but at times challenging to procure.

Since the entire monolith application runs as a single process, the scaling of individual features of the monolith is almost impossible. It internally supports a hardcoded number of connections and operations. However, scaling the entire application can be achieved by manually deploying a new instance of the monolith on another server, typically behind a load balancing appliance - another pricey solution.

Microservices can be deployed individually on separate servers provisioned with fewer resources - only what is required by each service and the host system itself, helping to lower compute resource expenses.

Although the distributed nature of microservices adds complexity to the architecture, one of the greatest benefits of microservices is scalability. With the overall application becoming modular, each microservice can be scaled individually, either manually or automated through demand-based autoscaling.

#### Container Orchestration

Container images allow us to confine the application code, its runtime, and all of its dependencies in a pre-defined format. 

https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2024/block-v1:LinuxFoundationX+LFS158x+1T2024+type@sequential+block@e10a62dcf641474c997eabd0602111cb/block-v1:LinuxFoundationX+LFS158x+1T2024+type@vertical+block@be9c2293aab04313bbb711e7c83ef91c