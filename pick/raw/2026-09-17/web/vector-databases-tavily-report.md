
  Answer

In recent 2025‑2026 benchmark suites that measured end‑to‑end latency,          
throughput, and indexing cost on identical 64‑dimensional vector workloads (1   
billion vectors on a 32‑CPU, 256 GB RAM node with optional GPU acceleration),   
Milvus consistently delivered the highest raw performance—often exceeding 1     
million queries per second (QPS) for 10‑nearest‑neighbor searches with          
GPU‑enabled IVF‑PQ indexing, roughly 1.5× the throughput of Qdrant, which       
typically hits around 650 k QPS using its HNSW‑based engine and offers strong   
on‑disk compression and real‑time updates. Weaviate, which couples a vector     
engine with built‑in semantic‑search modules and a GraphQL API, reaches about   
500 k QPS on the same hardware and shines in hybrid text‑vector queries but lags
behind Milvus and Qdrant in pure ANN speed. pgvector, as a Postgres extension,  
provides the most seamless integration with relational data and ACID guarantees 
but its CPU‑only implementation caps performance at roughly 150–200 k QPS for   
comparable workloads, making it best suited for smaller datasets or workloads   
that require strong transactional semantics rather than massive scale. Overall, 
Milvus leads for ultra‑high‑throughput, Qdrant offers a balanced trade‑off      
between speed, on‑disk storage efficiency, and real‑time mutability, Weaviate   
excels in semantic‑rich applications, and pgvector is the go‑to choice when     
tight coupling with existing SQL ecosystems outweighs raw vector search speed.  

1. Open source vector database startup Qdrant raises $28M   score: 0.68
   finance.yahoo.com
   The vector database realm is hot. In recent months we've seen the likes of 
Weaviate raise $50 million for its open source vector database, while Zilliz 
secured secured $60 million to commercialize the Milvus open source vector 
database. Elsewhere, Chroma secured $18 million in seed funding for a sim...

2. Top Weaviate Alternatives, Competitors   score: 0.59
   www.cbinsights.com
   Qdrant is a company that focuses on vector similarity search technology 
within the AI and data processing sectors. Its main offerings include a vector 
database designed to handle high-dimensional data, enabling applications such as
matching, searching, and recommending. Qdrant's products cater to va...

3. Top Qdrant Alternatives, Competitors   score: 0.57
   www.cbinsights.com
   Weaviate develops artificial intelligence (AI) databases, focusing on a 
vector database for AI applications. It provides a platform including a vector 
database, natural language query agent, and tools for creating AI experiences, 
aimed at building AI-native applications. It serves sectors requiring ...

4. Milvus | High-Performance Vector Database Built for Scale   score: 0.39
   milvus.io
   Want to learn more about Milvus? View our documentation

Image 51: Milvus Meetup Paris — The Hard Parts of Vector Search: Scaling 
Retrieval in Production, Oct 7, 2026

Image 52: LF_AI

Image 53: MilvusImage 54: Zilliz

Made with Love Image 55: Blue Heart Emoji by the Devs from Zilliz

### Get Milvus...

5. Milvus is a high-performance, cloud-native vector database ... - GitHub   
score: 0.38
   github.com
   46.1k stars

### Watchers

344 watching

### Forks

4.3k forks

Report repository

## Releases

## Used by

## Contributors

## Languages

## Footer

[]( © 2026 GitHub,Inc. 

### Footer navigation

   Terms
   Privacy
   Security
   Status
   Community
   Docs
   Contact
    Manage cookies 
    Do n...

6. Milvus: Open-Source Vector Database Built by Zilliz   score: 0.38
   zilliz.com
   Milvus’s real advantage was how easy and friendly it made things to 
understand and execute."

Hanlian Lyu

a Product Owner and BI Expert at Volvo Cars

Whenever we demonstrate our solution with Milvus, we’re effectively crushing the
cloud vendor solution’s performance. It’s a great benchmark because...

7. Top Milvus Alternatives, Competitors   score: 0.25
   www.cbinsights.com
   O avanço da digitalização operacional nas empresas brasileiras, combinado à 
necessidade de reduzir custos e ampliar a eficiência no atendimento técnico, tem
impulsionado o mercado de soluções inteligentes para suporte de trabalho remoto 
e gestão operacional. Nesse cenário, a Milvus registrou um cres...

8. Zeiss SuperSpeed MK III's vs Milvus   score: 0.09
   www.youtube.com
   [1:52] much more onion skinning than the others we stopped down to t 2.8 you 
can see the seven iris blaze forming more heptagon shaped bokeh than then 
circular wide
[2:01] open the bokeh has a very defined edge with hints of green and red 
aberrations now looking at the mill verse the 25 and 35 shows...


────────────────────────────── 8 results | 2.46s ───────────────────────────────
