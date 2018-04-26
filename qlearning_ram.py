import numpy as np

#load file

file = np.loadtxt("DataTugasML3.txt")
#reward
reward = np.array(file).astype("int")
tbl_Q = np.zeros((4,100),dtype=int) #set nilai Q = 0

def insert_q(state, next_state, action):
    gamma = 0.5
    alpha = 1
    qsa = tbl_Q[state,action]
    Q_baru = state + alpha * (reward[state,action] + gamma * max(tbl_Q[next_state: ]) - qsa)
    print("state",qsa)

#Main
# print(reward)
print("Posisi Agent = ",reward[9][0]) #baris x kolom
jum_episode = 5
jum_state = 100
jum_aksi = 4 #0 = North (Atas) 1 = East (Kanan) 2 = South (Bawah) 3= West (Kiri)
# acak_s = np.random.RandomState(80)
finish = False
acak = np.random.RandomState()

#create episode
for eps in range(int(jum_episode)):
    pos_awal = [0,0]
    while not finish:
        pilihan_aksi = np.array(list(range(jum_aksi)))
        pilih_aksi = np.random.choice(pilihan_aksi)
        aksi_terpilih = pilih_aksi
        next_state = aksi_terpilih
        # print(eps)
        finish = True
        print("aksi = ", pilih_aksi)
        new_reward = insert_q(pos_awal,next_state,aksi_terpilih)
