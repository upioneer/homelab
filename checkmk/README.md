check**mk** Raw one liner
```yml
docker container run -dit -p 8080:5000 -p 8000:8000 --tmpfs /opt/omd/sites/cmk/tmp:uid=1000,gid=1000 -v monitoring:/omd/sites --name monitoring -v /etc/localtime:/etc/localtime:ro --restart always checkmk/check-mk-raw:2.4.0p11
```
I created a docker-compose.yml from the one liner
```yml
services:
  monitoring:
    image: checkmk/check-mk-raw:2.4.0p11
    container_name: monitoring
    restart: unless-stopped
    ports:
      - "8080:5000"
      - "8000:8000"
    tmpfs:
      - /opt/omd/sites/cmk/tmp:uid=1000,gid=1000
    volumes:
      - monitoring:/omd/sites
      - /etc/localtime:/etc/localtime:ro

volumes:
  monitoring:
```
