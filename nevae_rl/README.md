## Instructions to run the code

# 
- Please train the original NeVAE model and store the model in a directory
- Supply the directory as `restore_dir` in the follwing command

```
usage: main.py [-h] [--num_epochs NUM_EPOCHS] [--learning_rate LEARNING_RATE]
               [--decay_rate DECAY_RATE] [--dropout_rate DROPOUT_RATE]
               [--log_every LOG_EVERY] [--sample_file SAMPLE_FILE]
               [--random_walk RANDOM_WALK] [--z_dim Z_DIM] [--nodes NODES]
               [--bin_dim BIN_DIM] [--temperature TEMPERATURE]
               [--synthetic SYNTHETIC] [--graph_file GRAPH_FILE]
               [--z_dir Z_DIR] [--sample SAMPLE] [--mask_weight MASK_WEIGHT]
               [--out_dir OUT_DIR] [--restore_dir RESTORE_DIR]
               [--neg_sample_size NEG_SAMPLE_SIZE] [--node_sample NODE_SAMPLE]
               [--bfs_sample BFS_SAMPLE] [--E E] [--no_traj NO_TRAJ]

optional arguments:
  -h, --help            show this help message and exit
  --num_epochs NUM_EPOCHS
                        Number of epochs
  --learning_rate LEARNING_RATE
                        learning rate
  --decay_rate DECAY_RATE
                        decay rate
  --dropout_rate DROPOUT_RATE
                        dropout rate
  --log_every LOG_EVERY
                        write the log in how many iterations
  --sample_file SAMPLE_FILE
                        directory to store the sample graphs
  --random_walk RANDOM_WALK
                        random walk depth
  --z_dim Z_DIM         z_dim
  --nodes NODES         z_dim
  --bin_dim BIN_DIM     bin_dim
  --temperature TEMPERATURE
                        temperature
  --synthetic SYNTHETIC
                        synthetic or real
  --graph_file GRAPH_FILE
                        The dictory where the training graph structure is
                        saved
  --z_dir Z_DIR         The z values will be stored file to be stored
  --sample SAMPLE       True if you want to sample
  --mask_weight MASK_WEIGHT
                        True if you want to mask weight
  --out_dir OUT_DIR     Store log/model files.
  --restore_dir RESTORE_DIR
                        Restore weight values from NeVAE.
  --neg_sample_size NEG_SAMPLE_SIZE
                        number of negative edges to be sampled
  --node_sample NODE_SAMPLE
                        number of nodes to be sampled
  --bfs_sample BFS_SAMPLE
                        number of times bfs to run
  --E E                 number of edges to be fixed
  --no_traj NO_TRAJ     number of trajectories to be sampled
```

- once trained, get the generated molecule and follow nevae_3d instructions for 3d molecule generation
