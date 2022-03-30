FROM confluentinc/cp-kafka-connect:6.2.0

RUN confluent-hub install debezium/debezium-connector-postgresql:latest --no-prompt
RUN confluent-hub install confluentinc/kafka-connect-datagen:latest --no-prompt
