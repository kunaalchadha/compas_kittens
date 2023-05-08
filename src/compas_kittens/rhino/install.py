from compas.plugins import plugin

@plugin(category='install')
def installable_rhino_packag():
    return ["compas_kittens"]
