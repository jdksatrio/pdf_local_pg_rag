# pdf_local_pg_rag

A RAG system built on Phidata framework, embed local PDFs using local Ollama and store it on local PG (running on Docker)

docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16


# connection_test_groq

To check connection to Groq
