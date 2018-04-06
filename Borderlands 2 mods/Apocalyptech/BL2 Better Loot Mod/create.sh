./generate-source.py && (
    PROFILES=("Lootsplosion" "Reasonable Drops")
    VARIANTS=("UCP Compat" "Standalone" "Standalone Offline")
    for PROFILE in "${PROFILES[@]}"
    do
        for VARIANT in "${VARIANTS[@]}"
        do
            ../conv_to_mod.py -f "BL2 Better Loot Mod ($PROFILE) - $VARIANT" || exit
        done
    done
    )
