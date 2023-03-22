import sys
sys.path.append('..')
import qwalk.coined.segment as hp_seg
import plot as hplot


seg = hp_seg.Segment(10)
state = seg.state([(1, 0, 0)])
S = seg.persistent_shift_operator()

sim_psi = seg.simulate_walk(S, state, 15, save_interval=1)
probs = seg.probability_distribution(sim_psi)

hplot.plot_probability_distribution(probs, animate=True, show=False,
                                    filename_prefix="coined_segment")
