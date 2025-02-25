(load "global_path.clp")
(bind ?*path* (str-cat ?*path* "/src/clp_files/bind-tense-etc.clp"))
(load ?*path*)
(load-facts "hin-clips-facts.dat")
(load-facts "updated_mrs_feature_info.dat")
(open "bind-mrs-tense-etc.dat" open-tense "w")
(open "bind-mrs-tense-etc_debug.dat" debug_tense "w")
(watch rules)
(watch facts)
(agenda)
