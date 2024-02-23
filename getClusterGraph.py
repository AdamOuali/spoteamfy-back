from getFeatures import getFeatures
from predict import predict_cluster


def getClusterGraph(token):
    features = getFeatures(token)
    graph_data = predict_cluster(features)
    # graph_data["animal_cluster"] = faire la moyenne du tableau dans "user_cluster"
    values_of_user_cluster = graph_data["user_cluster"]
    graph_data["animal_cluster"] = sum(values_of_user_cluster) / len(
        values_of_user_cluster
    )
    # arrondir en int
    graph_data["animal_cluster"] = int(graph_data["animal_cluster"])
    return graph_data
