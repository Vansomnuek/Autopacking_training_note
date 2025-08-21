# WCS Modbus TCP communication
## Familiarize with the Modbus TCP protocol used for communication with Yongchuang equipment

**Date:** YYYY-MM-DD  
**Trainer:** (Name)

---

### 🧑‍💻 Natthawut
> No comment


---

### 🧑‍💻 Sikarin
> No comment


---

### 🧑‍💻 Suraphop
> No comment


---

### 🧑‍💻 Van

## 1. Box assembly
- The empty box assembly machine communicates with the WCS using Modbus TCP
- The WCS sends this message {ActionID : 1-15 , Location: 1-6 , Qty : ...} to the empty box assembly machine every 3 seconds. Once the machine receives the command, it sends back the status 666 to the WCS to indicate that the machine has started.
