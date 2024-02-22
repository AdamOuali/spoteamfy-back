from getFeatures import getFeatures
from predict import predict_cluster


def getClusterGraph(token):
    features = getFeatures(token)
    graph_data = predict_cluster(features)
    return graph_data
