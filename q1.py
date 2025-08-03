import math

def sigmoid(z):
    """
    Calculate the sigmoid activation function.
    
    Args:
        z (float): Input value to the sigmoid function
        
    Returns:
        float: Output of sigmoid function (1 / (1 + e^-z))
    """
    return 1 / (1 + math.exp(-z))

def calculate_neuron_output(x1, x2, w1, w2, bias):
    """
    Calculate the output of a single neuron using sigmoid activation.
    
    Args:
        x1, x2 (float): Input values
        w1, w2 (float): Corresponding weights
        bias (float): Bias value
        
    Returns:
        float: Neuron output after sigmoid activation
    """
    # Calculate weighted sum with bias
    z = x1 * w1 + x2 * w2 + bias
    
    # Apply sigmoid activation function
    output = sigmoid(z)
    
    return output

def main():
    """
    Main function to get user input and calculate neuron output.
    """
    try:
        # Get input values from user
        print("Enter the input values and parameters for the neuron:")
        
        # Get input values
        x1, x2 = map(float, input("Enter x1, x2: ").split())
        
        # Get weights
        w1, w2 = map(float, input("Enter w1, w2: ").split())
        
        # Get bias
        bias = float(input("Enter bias: "))
        
        # Calculate neuron output
        output = calculate_neuron_output(x1, x2, w1, w2, bias)
        
        # Display result rounded to 3 decimal places
        print(f"\nNeuron output: {output:.3f}")
        
        # Optional: Show intermediate calculation
        z = x1 * w1 + x2 * w2 + bias
        print(f"Intermediate calculation: z = {x1}*{w1} + {x2}*{w2} + {bias} = {z:.3f}")
        print(f"Sigmoid(z) = 1 / (1 + e^-{z:.3f}) = {output:.3f}")
        
    except ValueError:
        print("Error: Please enter valid numerical values.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
