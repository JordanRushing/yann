from yann.network import network
from yann.utils.graph import draw_network    

def log_reg ( dataset, verbose ):            
    """
    This function is a demo example of multi-layer neural networks  from the infamous paper by 
    Yann LeCun. This is an example code. You should study this code rather than merely run it.  

    """
    dataset_params  = {
                            "dataset"   :  dataset,
                            "svm"       :  False, 
                            "n_classes" : 10,
                            "id"        : 'data',
                    }


    # intitialize the network
    net = network( verbose = verbose )                       
    
    # or you can add modules after you create the net.
    net.add_module ( type = 'datastream', 
                     params = dataset_params,
                     verbose = verbose )

    # add an input layer 
    net.add_layer ( type = "input",
                    id = "input",
                    verbose = verbose, 
                    datastream_origin = 'data', 
                    # if you didnt add a dataset module, now is the time. 
                    mean_subtract = False )
    
    net.add_layer ( type = "classifier",
                    id = "softmax",
                    origin = "input",
                    num_classes = 10,
                    activation = 'softmax',
                    verbose = verbose
                    )

    net.add_layer ( type = "objective",
                    id = "nll",
                    origin = "softmax",
                    objective = 'nll',
                    verbose = verbose
                    )

    # objective provided by classifier layer               
    # nll-negative log likelihood, 
    # cce-categorical cross entropy, 
    # bce-binary cross entropy,
    # hinge-hinge loss 
    learning_rates = (0.05, 0.01, 0.001)  
    # (initial_learning_rate, annealing, ft_learnint_rate)

    net.cook( objective_layer = 'nll',
              datastream = 'data',
              classifier = 'softmax',
              learning_rates = learning_rates,
              verbose = verbose
              )
    # visualization of the network.  
    # draw_network(net.graph, filename = 'log_reg.png')     
    net.pretty_print()
    net.train( epochs = (20, 20), 
               validate_after_epochs = 1,
               training_accuracy = True,
               show_progress = True,
               early_terminate = True,
               verbose = verbose)
               
    net.test( show_progress = True,
               verbose = verbose)


## Boiler Plate ## 
if __name__ == '__main__':
    dataset = None  
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'create_dataset':
            from yann.special.datasets import cook_mnist  
            data = cook_mnist (verbose = 3)
            dataset = data.dataset_location()
        else:
            dataset = sys.argv[1]
    else:
        print "provide dataset"
    
    if dataset is None:
        print " creating a new dataset to run through"
        from yann.special.datasets import cook_mnist  
        data = cook_mnist (verbose = 3)
        dataset = data.dataset_location()

    log_reg ( dataset, verbose = 2 ) 

