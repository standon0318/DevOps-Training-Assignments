From ubuntu:14.04
Maintainer shashank tandon <standon@gmail.com>
#add java class files
ADD ./*.class . 
#install java 
RUN apt-get update 
RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update -y && apt-get install openjdk-8-jdk -y && \
    apt-get clean
#run container
CMD ["java","HELLOWORLD"]



