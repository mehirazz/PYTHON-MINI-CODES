
global_var = "I am a Global Variable"

def show_variables():
  
    local_var = "I am a Local Variable"
    
    print("Inside Function:")
    print(global_var)  
    print(local_var)   

show_variables()

print("\nOutside Function:")
print(global_var)  
