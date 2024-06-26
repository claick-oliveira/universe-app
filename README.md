# universe-app

## Commands

```bash
docker run --name local-psql -v local_psql_data:/var/lib/postgresql/data -p 54320:5432 -e POSTGRES_PASSWORD=my_password -d postgres
```

```bash
docker exec -it local-psql psql -U postgres
```

```bash
CREATE DATABASE universe;
\c universe
```

```bash
create user appuser with encrypted password 'apppass';
grant all privileges on database universe to appuser;
grant all on schema public to appuser;
```

To Run the Server in Terminal

```bash
flask run
```

To Run the Server with specific host and port `flask run -h HOSTNAME -p PORTNUMBER`

```bash
flask run -h 127.0.0.2 -p 5001
```

To Run the Server with Automatic Restart When Changes Occur

```bash
FLASK_DEBUG=1 flask run
```
