This directory contains mappings and files used by WireMock to mock
the MS for HMB testing.

To run:

   $ cd /opt/wiremock
   $ java -jar wiremock-1.48-standalone.jar --root-dir /opt/designchallenge2015/brata.station/wiremock --no-request-journal


To verify all stub mappings and verify WireMock is running:

   $ curl http://localhost:8080/__admin

To verify API:

   $ curl -X POST --header 'Accept: application/json' --data '{"message_version": 0, "message_timestamp": "2014-09-15 14:08:59", "station_instance_id": "97531", "station_type": "hmb", "station_host": "192.168.0.2", "station_port", "9876"}' http://localhost:8080/ms/1.0.0/connect
