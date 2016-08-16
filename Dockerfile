# Minimal example, any base image will do
FROM jboss-amq-6/amq62-openshift

# Using e.g. Dogen would tidy up the USER stuff
USER root
ADD *py /usr/local/bin/
RUN chmod +x /usr/local/bin/*py
RUN ["/usr/local/bin/jammasterw-bin.py", "--build"]
USER jboss
ENTRYPOINT ["/usr/local/bin/jammasterw-bin.py"]

# Shame we have to redeclare CMD, really we just want base image's
CMD [ "/opt/amq/bin/activemq", "console" ]
