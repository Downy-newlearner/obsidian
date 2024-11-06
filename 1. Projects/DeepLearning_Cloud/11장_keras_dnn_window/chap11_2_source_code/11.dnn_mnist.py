# summarize history for accuracy
plt.plot(disp.history['accuracy'])
plt.plot(disp.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')

# Save the accuracy plot
plt.savefig("C:/Obsidian/obsidian/1. Projects/DeepLearning_Cloud/11장_keras_dnn_window/chap11_2_source_code/dnn_mnist_performance_result/model_accuracy.png")
plt.show()

# summarize history for loss
plt.plot(disp.history['loss'])
plt.plot(disp.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')

# Save the loss plot
plt.savefig("C:/Obsidian/obsidian/1. Projects/DeepLearning_Cloud/11장_keras_dnn_window/chap11_2_source_code/dnn_mnist_performance_result/model_loss.png")
plt.show()
