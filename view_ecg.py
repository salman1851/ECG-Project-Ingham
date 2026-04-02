import glob

########## FIND LEADS NPY ##########

filelist = glob.glob("/mnt/Cardiology_ECG/OutputData/ProcessedAttachments/**/leads.npy")

import numpy as np # open npy lead

# leads_found = []
# for i in range(len(filelist)):
#     sample_file = filelist[i]
#     sample_lead = np.load(sample_file, allow_pickle=True)
#     object_deref = sample_lead[()]
#     num_leads = len(object_deref)
#     leads_found.append(num_leads)

# print("Average number of leads found in numpy files = ", np.mean(leads_found))

########## VISUALIZE ONE SAMPLE ##########

import matplotlib.pyplot as plt

sample_file = filelist[0]
sample_leads = np.load(sample_file, allow_pickle=True)
leads_dict = sample_leads[()]
lead_names = list(leads_dict.keys())

fig, axes = plt.subplots(6, 2, figsize=(12,10), sharex=True, sharey=True)
axes = axes.ravel()

for idx, name in enumerate(lead_names):
    curr_lead = leads_dict[name]
    t = curr_lead['t_s']
    v = curr_lead['v_mV']

    ax = axes[idx]
    ax.plot(t, v, linewidth=0.8)
    ax.set_title(name)
    ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig("../OutputData/LeadPlots/leads.jpg", dpi=300, bbox_inches="tight")
plt.close(fig)