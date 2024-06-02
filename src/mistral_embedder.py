import os

from haystack_integrations.components.embedders.mistral.document_embedder import MistralDocumentEmbedder
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack import Document, Pipeline
from haystack.components.writers import DocumentWriter

document_store = InMemoryDocumentStore(embedding_similarity_function="cosine")

documents = [Document(content="My name is Wolfgang and I live in Berlin"), 
             Document(content="I saw a black horse running"),
             Document(content="Germany has many big cities")] 

embedder = MistralDocumentEmbedder()
writer = DocumentWriter(document_store=document_store)
        
indexing_pipeline = Pipeline()
indexing_pipeline.add_component(name="embedder", instance=embedder)
indexing_pipeline.add_component(name="writer", instance=writer)
indexing_pipeline.connect("embedder", "writer")


indexing_pipeline.run(data={"embedder": {"documents": documents}})