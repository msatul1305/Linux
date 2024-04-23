```mermaid
erDiagram
    CUSTOMER }|..|{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER ||--o{ INVOICE : "liable for"
    INVOICE ||--|{ LINE-ITEM : "includes"
    LINE-ITEM }|..|{ PRODUCT : "consists of"
```
