# prompt-diary
Prompt diary

## Description
Just a simple prompt aplication to test some functions of python and psychopg2

### Technologies Used

- Python 3.10
- Psychopg2 2.9.6
- PostgreSQL 15.3
- Docker 24.0.2

## How to run

1. Clone this repository

```bash
git clone git@github.com:davi-marangoni/prompt-diary.git
```

2. Install the psycopg2 library

```bash
pip install psycopg2
```

3. Install Docker and Docker Compose

```bash
 sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
 sudo apt-get install docker-compose-plugin
```

4. Create the docker.compose.yml file and run

```bash
version: '3'
services:
  postgres:
    image: postgres:latest
    restart: always
    ports:
      - '5432:5432'
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=postgres
    volumes:
      - ./data:/var/lib/postgresql/data
```
```bash
docker-compose up -d
```

5. Create the database and table's

```bash
CREATE DATABASE diary;

CREATE TABLE public.events (
	event_id serial4 NOT NULL,
	event_description text NULL,
	event_date timestamp NULL,
	CONSTRAINT events_pkey PRIMARY KEY (event_id)
);
```