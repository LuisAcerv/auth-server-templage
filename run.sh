
#!/bin/bash

serve(){
    gunicorn -b 0.0.0.0:5000 app.app:app --reload             
}

serve

