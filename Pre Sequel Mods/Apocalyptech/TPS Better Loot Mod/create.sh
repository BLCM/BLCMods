./generate-source.py && (
    PROFILES=("Lootsplosion" "Reasonable Drops")
    VARIANTS=("UCP Compat" "Standalone Offline")
    for PROFILE in "${PROFILES[@]}"
    do
        for VARIANT in "${VARIANTS[@]}"
        do
            ../../../Borderlands\ 2\ mods/Apocalyptech/conv_to_mod.py -f "TPS Better Loot Mod ($PROFILE) - $VARIANT" || exit
        done
    done
    )
