# Shows metrics during training process
import keras
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import os  # os 모듈 추가

class TrainingPlot(keras.callbacks.Callback):
    
    # This function is called when the training begins
    def on_train_begin(self, logs={}):
        # Initialize the lists for holding the logs, losses and accuracies
        self.losses = []
        self.acc = []
        self.val_losses = []
        self.val_acc = []
        self.logs = []
    
    # This function is called at the end of each epoch
    def on_epoch_end(self, epoch, logs={}):
        
        # Append the logs, losses and accuracies to the lists
        self.logs.append(logs)
        self.losses.append(logs.get('loss'))
        self.acc.append(logs.get('accuracy'))
        self.val_losses.append(logs.get('val_loss'))
        self.val_acc.append(logs.get('val_accuracy'))
        
        # Before plotting ensure at least 2 epochs have passed
        if len(self.losses) > 1:
            
            # Clear the previous plot
            clear_output(wait=True)
            N = np.arange(0, len(self.losses))
            
            # You can choose the style of your preference
            plt.style.use("ggplot")  # 변경된 스타일
            
            # Plot train loss, train acc, val loss and val acc against epochs passed
            plt.figure()
            plt.plot(N, self.acc, label="train_acc")
            plt.plot(N, self.val_acc, label="val_acc")
            plt.title("Training Loss and Accuracy [Epoch {}]".format(epoch))
            plt.xlabel("Epoch #")
            plt.ylabel("Loss/Accuracy")
            plt.legend()

            # Save the figure
            save_path = "C:/Obsidian/obsidian/1. Projects/DeepLearning_Cloud/11장_keras_dnn_window/chap11_2_source_code/dnn_mnist_performance_result"
            if not os.path.exists(save_path):
                os.makedirs(save_path)  # 디렉토리 생성
            plt.savefig(os.path.join(save_path, f'training_performance_epoch_{epoch}.png'))
            plt.close()  # 현재 플롯 닫기
