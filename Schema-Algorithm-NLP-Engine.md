# Goal: Schema and Algorithm Logic for NLP Engine
## T5 based NLP Query Parser for Housing Query
This document describes the schema and algorithmic workflow for an NLP engine designed to parse housing-related user queries. The model combines a T5 transformer with rule-based logic to extract structured parameters from natural-language input.
The output format is JSON, enabling downstream systems (recommedener system) to consume standardized housing search parameters (for example: priority, location, budget, room count, rental/sale type, and other constraints).
## Flowchart

```mermaid

%%{init: {
  'theme': 'default',
  'themeVariables': {
    'fontSize': '12px',
    'nodeSpacing': 15,
    'rankSpacing': 10
  },
  'flowchart': {
    'curve': 'linear'
  }
}}%%

flowchart TD
    %% Top-level steps
    A0["Step 0 — User Input Reception"]
    A1["Step 1 — Text Preprocessing       (rule-based normalization)" ]
    A2["Step 2 a — Feature Extraction (prompt template construction:instruction + target format)"]
    A3["Step 2 b - Feature Extraction (T5 tokenizer,Tokenization and Labeling Mapping)"]
    
    %% Training process
    A4["Step 3- Load T5 Base Model"]
    A5["Step 4- LoRA Fine Tuning"]
   
    %% Intent classfication
    B1["Step Optional- Intent classification(T5, renting species)"]
   

    %% Parallel extraction branches
    C1["Step 5a — Rule-based Entity Extraction: clear value + parameters"]
    C2["Step 5b — T5-based Entity Extraction : vauge, context-aware"]
    
    %% Merging and final steps
    D1["Step 6 — Entity Merge & Parameter Mapping : rule based overwrite the t5 based entity"]

    %% Ouput Corrections
    E1["Step 7— Direct JSON Parse"]
    E2["Step 8 — JSON Repair /Fallback(regex, cleanup)"]

    %% Final
    F0["Step 9-Final Json Output"]
    
    %% Flow
    A0 --> A1 --> A2 --> A3 --> A4-->A5--> B1
    
    B1 --> C1
    B1 --> C2
    C1--> D1
    C2--> D1
    D1 --> E1
    D1 --> E2
    E1 -->  F0
    E2 -->  F0
    


    %% Styling
    classDef input fill:#ffe7d6,stroke:#d35400,color:#4a2500;
    classDef preprocess fill:#ffeed6,stroke:#bf7100,color:#4a3100;
    classDef process fill:#e7f2ff,stroke:#0057b8,color:#002855;
    classDef lora fill:#fff3cd,stroke:#f5a623,color:#7a4f01;
    classDef extract fill:#d4f8d4,stroke:#2b9348,color:#145a32;
    classDef repair fill:#fde2e4,stroke:#c1121f,color:#5a0000;
    classDef output fill:#e6ffe7,stroke:#38a169,color:#1f542b;
    classDef role fill:#ccffec,stroke:#00b386, color:#000594d;



    class A0 input;
    class A1 preprocess;
    class A2,A3,B1 process;
    class A4,A5 role;
    class C1,C2 extract;
    class D1 extract;
    class E1,E2 repair;
    class F0 output;

    

```
## Algorithmic Overview
